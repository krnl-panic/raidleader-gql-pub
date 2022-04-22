from api.models import Loot
from .base import BaseLoader


class LootLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.batch_loader(keys, db_session=self.db_session)

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
        return self.load(context.loot_id)


class AuctionLootsLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.child_batch_loader(
            keys, parent_id_field="auction_id", db_session=self.db_session
        )

    def resolver(self, _context, _info, *, auction_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param auction_id:

        """
        return self.load(auction_id)


class RaidLootsLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.child_batch_loader(
            keys, parent_id_field="raid_id", db_session=self.db_session
        )

    def resolver(self, _context, _info, *, raid_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param raid_id:

        """
        return self.load(raid_id)
