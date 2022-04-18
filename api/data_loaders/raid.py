from api.models import Raid
from .base import BaseLoader


class RaidLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """ """
        return await Raid.batch_loader(keys, db_session=self.db_session)

    def resolver(self, _context, _info, id):
        """  """
        return self.load(id)

    def context_resolver(self, model_dict: dict[str:any]):
        """ """
        return self.load(model_dict["raid_id"])
