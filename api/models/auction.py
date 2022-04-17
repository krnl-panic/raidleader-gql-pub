from api.database import db


class Auction(db.Model):
    """ """

    __tablename__ = "auction"
    session_id = db.Column(db.Integer, db.ForeignKey("auction_session.id"))

    # price = db.Column(db.Integer)
    # winner_id = db.Column(db.Integer, db.ForeignKey("character.id"))

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "session_id": self.session_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
