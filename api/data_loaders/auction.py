from api.models import Auction
from .base import BaseLoader


class AuctionLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Auction.batch_loader(keys, db_session=self.db_session)

    def resolver(self, _context, _resolve_info, *, id):
        """

        :param _context: param _resolve_info:
        :param _resolve_info:
        :param *:
        :param id:

        """
        return self.load(id)

    def context_resolver(self, context, _resolve_info):
        """

        :param context: param _resolve_info:
        :param _resolve_info:

        """
        return self.load(context.auction_id)


class SessionAuctionsLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Auction.child_batch_loader(keys, parent_id_field="session_id", db_session=self.db_session)

    def resolver(self, _context, _resolve_info, *, session_id):
        """

        :param _context: param _resolve_info:
        :param _resolve_info:
        :param *:
        :param session_id:

        """
        return self.load(session_id)
