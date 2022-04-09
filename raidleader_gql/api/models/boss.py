from raidleader_gql import db
from aiodataloader import DataLoader


class Boss(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    items = db.relationship("Item", backref="boss", lazy=True)
    instance_id = db.Column(db.Integer, db.ForeignKey("instance.id"), nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=db.func.now()
    )
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
            "deletedAt": self.deleted_at,
        }

    @staticmethod
    def loader():
        """ """
        return BossLoader()


class BossLoader(DataLoader):
    """ """

    def batch_load_fn(self, keys):
        return Boss.batch_loader(keys)
