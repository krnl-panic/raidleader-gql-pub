from aiodataloader import DataLoader
from api.models import Instance


class InstanceLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Instance.batch_loader(keys)

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
        return self.load(context.instance_id)
