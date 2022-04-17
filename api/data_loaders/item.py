from aiodataloader import DataLoader
from api.models import Item


class ItemLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Item.batch_loader(keys)

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
        return self.load(context.item_id)


class BossItemsLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Item.child_batch_loader(keys, parent_id_field="boss_id")

    def resolver(self, _context, _info, *, boss_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param boss_id:

        """
        return self.load(boss_id)
