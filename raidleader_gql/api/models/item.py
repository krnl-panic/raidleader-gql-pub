from raidleader_gql import db
from aiodataloader import DataLoader


class Item(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    boss_id = db.Column(db.Integer, db.ForeignKey("boss.id"))
    instance_id = db.Column(db.Integer, db.ForeignKey("instance.id"))
    wowhead_url = db.Column(db.String)
    wow_id = db.Column(db.Integer, nullable=False)

    instance = db.relationship("Instance", backref="items", lazy=True)

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
            "wowhead_url": self.wowhead_url,
            "boss": self.boss,
            "wowId": self.wow_id,
            "instance": self.instance,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }

    @staticmethod
    def loader():
        """ """
        return ItemLoader()


class ItemLoader(DataLoader):
    """ """

    def batch_load_fn(self, keys):
        return Item.batch_loader(keys)
