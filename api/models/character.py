from app import db
from aiodataloader import DataLoader
import enum

class PlayerClassEnum(enum.Enum):
    druid = 'druid'
    mage = 'mage'
    hunter = 'hunter'
    rogue = 'rogue'
    shaman = 'shaman'
    paladin = 'paladin'
    priest = 'priest'
    warrior = 'warrior'
    warlock = 'warlock'
    deathknight = 'deathknight'

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    player_class = db.Column(db.Enum(PlayerClassEnum), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "player_class": self.player_class,
            "user": self.user,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        return CharacterLoader()

class CharacterLoader(DataLoader):
    async def batch_load_fn(self, keys):
        return await Character.batch_loader(keys)
