from app import db
from aiodataloader import DataLoader

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    discord_id = db.Column(db.BigInteger, nullable=False)
    discord_username = db.Column(db.String, nullable=False)
    characters = db.relationship('Character', backref='user', lazy=True)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "discord_id": self.discord_id,
            "discord_username": self.discord_username,
            "characters": self.characters,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        return UserLoader()

class UserLoader(DataLoader):
    async def batch_load_fn(self, keys):
        return await User.batch_loader(keys)
