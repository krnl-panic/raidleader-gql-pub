from api.models import Boss
from .base import BaseLoader


class BossLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Boss.batch_loader(keys, db_session=self.db_session)

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


class InstanceBossesLoader(BaseLoader):
    """ """

    async def batch_load_fn(self, keys):
        """

        :param keys:

        """
        return await Boss.child_batch_loader(
            keys, parent_id_field="instance_id", db_session=self.db_session
        )

    def resolver(self, _context, _info, *, instance_id):
        """

        :param _context: param _info:
        :param _info:
        :param *:
        :param instance_id:

        """
        return self.load(instance_id)
