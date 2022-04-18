from sqlalchemy import Column, Integer, ForeignKey

from api.database import BaseModel


class AuctionSession(BaseModel):
    """ """

    __tablename__ = "auction_session"
    raid_id = Column(Integer, ForeignKey("raid.id"))

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "raid_id": self.raid_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
