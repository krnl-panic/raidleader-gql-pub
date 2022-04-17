from aiodataloader import DataLoader
from api.models import Boss


class BossLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Boss.batch_loader(keys)

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
        return self.load(context.boss_id)


class InstanceBossesLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Boss.child_batch_loader(keys, parent_id_field="instance_id")

    def resolver(self, _context, _info, *, instance_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param instance_id:

        """
        return self.load(instance_id)
