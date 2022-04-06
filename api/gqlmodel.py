from flask_sqlalchemy import Model
from sqlalchemy import and_


class GQLModel(Model):
    """ """

    @classmethod
    async def batch_loader(cls, keys):
        model_ids = [int(key) for key in keys]
        model_id = cls.id
        deleted_at = cls.deleted_at
        query = cls.query.filter(and_(model_id.in_(model_ids), deleted_at is None))
        return [model for model in query.all()]
