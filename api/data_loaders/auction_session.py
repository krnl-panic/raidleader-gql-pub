from aiodataloader import DataLoader
from api.models import AuctionSession


class AuctionSessionLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await AuctionSession.batch_loader(keys)

    def resolver(self, _context, _info, *, id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param id:

        """
        return self.load(id)

    def context_resolver(self, context):
        """

        :param context:

        """
        return self.load(context.session_id)


class RaidAuctionSessionsLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await AuctionSession.child_batch_loader(keys, parent_id_field="raid_id")

    def resolver(self, _context, _info, *, raid_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param raid_id:

        """
        return self.load(raid_id)

    def context_resolver(self, context):
        """

        :param context:

        """
        return self.load(context.session_id)
