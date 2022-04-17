from api.database import db


class Loot(db.Model):
    """ """

    __tablename__ = "loot"
    raid_id = db.Column(db.Integer, db.ForeignKey("raid.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    auction_id = db.Column(db.Integer, db.ForeignKey("auction.id"))

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "raid_id": self.raid_id,
            "item_id": self.item_id,
            "auction_id": self.auction_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
