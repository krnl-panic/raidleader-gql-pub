from aiodataloader import DataLoader
from api.models import Loot


class LootLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.batch_loader(keys)

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


class AuctionLootsLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.child_batch_loader(keys, parent_id_field="auction_id")

    def resolver(self, _context, _info, *, auction_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param auction_id:

        """
        return self.load(auction_id)


class RaidLootsLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Loot.child_batch_loader(keys, parent_id_field="raid_id")

    def resolver(self, _context, _info, *, raid_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param raid_id:

        """
        return self.load(raid_id)
