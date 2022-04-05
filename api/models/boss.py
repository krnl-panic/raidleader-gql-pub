from aiodataloader import DataLoader

from app import db


class Boss(db.Model):
    """ """
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    items = db.relationship('Item', backref='boss', lazy=True)
    instance_id = db.Column(
        db.Integer,
        db.ForeignKey('instance.id'),
        nullable=False)

    created_at = db.Column(
        db.DateTime(
            timezone=True),
        nullable=False,
        server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(
            timezone=True),
        nullable=False,
        server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))

    def to_dict(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "instance": self.instance,
            "items": self.items,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        """ """
        return BossLoader()


class BossLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        return await Boss.batch_loader(keys)
