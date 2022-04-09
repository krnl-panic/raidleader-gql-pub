from flask_sqlalchemy import Model as SQLModel


class Model(SQLModel):
    """ """

    @classmethod
    def batch_loader(cls, keys):
        print(Model.__name__)
        return [
            instance.to_dict()
            for instance in cls.query.filter(
                cls.id.in_(keys) and cls.deleted_at is None
            ).all()
        ]
