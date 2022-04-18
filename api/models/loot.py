from sqlalchemy import Column, Integer, ForeignKey

from api.database import BaseModel


class Loot(BaseModel):
    """ """

    __tablename__ = "loot"
    raid_id = Column(Integer, ForeignKey("raid.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    auction_id = Column(Integer, ForeignKey("auction.id"))

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
