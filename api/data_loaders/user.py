from aiodataloader import DataLoader
from api.models import User


class UserLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await User.batch_loader(keys)

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
        return self.load(context.user.id)
