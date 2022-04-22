from api.models import Item
from .base import BaseLoader


class ItemLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Item.batch_loader(keys, db_session=self.db_session)

    def resolver(self, _context, _info, id):
        """

        :param _context: param _info:
        :param id:
        :param _info:

        """
        return self.load(id)

    def context_resolver(self, model_dict: dict[str:any]):
        """ """
        return self.load(model_dict["item_id"])


class BossItemsLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Item.child_batch_loader(
            keys, parent_id_field="boss_id", db_session=self.db_session
        )

    def resolver(self, _context, _info, *, boss_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param boss_id:

        """
        return self.load(boss_id)
