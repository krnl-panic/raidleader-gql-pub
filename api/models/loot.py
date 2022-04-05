from aiodataloader import DataLoader

from app import db


class Loot(db.Model):
    """ """
    id = db.Column(db.Integer, primary_key=True)

    raid_id = db.Column(db.Integer, db.ForeignKey('raid.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    auction_id = db.Column(db.Integer, db.ForeignKey('auction.id'))

    item = db.relationship('Item', backref='loots', lazy=True)

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
            "raid": self.raid,
            "item": self.item,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        """ """
        return LootLoader()


class LootLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        return await Loot.batch_loader(keys)
