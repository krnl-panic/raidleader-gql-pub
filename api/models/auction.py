from sqlalchemy import Column, Integer, ForeignKey

from api.database import BaseModel


class Auction(BaseModel):
    """ """

    __tablename__ = "auction"
    session_id = Column(Integer, ForeignKey("auction_session.id"))

    # price = Column(Integer)
    # winner_id = Column(Integer, ForeignKey("character.id"))

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "session_id": self.session_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
