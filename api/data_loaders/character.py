from aiodataloader import DataLoader
from api.models import Character


class CharacterLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Character.batch_loader(keys)

    def resolver(self, _context, _info, id):
        """

        :param _context: param _info:
        :param id:
        :param _info:

        """
        return self.load(id)

    def context_resolver(self, context):
        """

        :param context:

        """
        return self.load(context.character_id)


class UserCharactersLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Character.child_batch_loader(keys, parent_id_field="user_id")

    def resolver(self, _context, _info, *, user_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param user_id:

        """
        return self.load(user_id)
