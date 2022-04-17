from api.database import db


class AuctionSession(db.Model):
    """ """

    __tablename__ = "auction_session"
    raid_id = db.Column(db.Integer, db.ForeignKey("raid.id"))

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "raid_id": self.raid_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
