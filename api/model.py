from flask_sqlalchemy import Model

class Model(Model):
    @classmethod
    async def batch_loader(keys):
        Model = __class__
        print(Model.__name__)
        return [
            instance.to_dict() 
            for instance in Model.query.filter(
                Model.id.in_(keys) and Model.deleted_at is None
            ).all()
        ]