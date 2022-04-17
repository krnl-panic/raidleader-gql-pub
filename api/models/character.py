import enum

from api.database import db


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


class Character(db.Model):
    """ """

    __tablename__ = "character"
    name = db.Column(db.String(128), nullable=False)
    player_class = db.Column(db.Enum(PlayerClassEnum), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "playerClass": self.player_class,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
