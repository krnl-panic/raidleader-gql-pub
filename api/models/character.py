import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from api.database import BaseModel


class PlayerClassEnum(enum.Enum):
    """ """

    druid = "druid"
    mage = "mage"
    hunter = "hunter"
    rogue = "rogue"
    shaman = "shaman"
    paladin = "paladin"
    priest = "priest"
    warrior = "warrior"
    warlock = "warlock"
    deathknight = "deathknight"


class Character(BaseModel):
    """ """

    __tablename__ = "character"
    name = Column(String(128), nullable=False)
    player_class = Column(Enum(PlayerClassEnum), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "playerClass": self.player_class.value,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
