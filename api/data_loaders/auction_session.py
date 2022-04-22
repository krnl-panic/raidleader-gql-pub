from api.models import AuctionSession
from .base import BaseLoader


class AuctionSessionLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await AuctionSession.batch_loader(keys, db_session=self.db_session)

    def resolver(self, _context, _info, *, id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param id:

        """
        return self.load(id)

    def context_resolver(self, model_dict):
        """ """
        return self.load(model_dict["session_id"])


class RaidAuctionSessionsLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await AuctionSession.child_batch_loader(
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

    def context_resolver(self, model_dict):
        """

        :param model_dict:

        """
        return self.load(model_dict["raid_id"])
