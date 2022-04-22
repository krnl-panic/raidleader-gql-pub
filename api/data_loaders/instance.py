from api.models import Instance
from .base import BaseLoader


class InstanceLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Instance.batch_loader(keys, db_session=self.db_session)

    def resolver(self, _context, _info, *, id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param id:

        """
        return self.load(id)

    def context_resolver(self, model_dict):
        """

        :param model_dict:

        """
        return self.load(model_dict["instance_id"])
