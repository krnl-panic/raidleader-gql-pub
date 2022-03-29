from app import db
from aiodataloader import DataLoader

class Raid(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
    instance_id = db.Column(db.Integer, db.ForeignKey('instance.id'), nullable=False)
   
    instance = db.relationship('Instance', backref='raids', lazy=True)
    auction_sessions = db.relationship('AuctionSession', backref='raid', lazy=True)
    loots = db.relationship('Loot', backref='raid', lazy=True)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "instance": self.instance,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        return RaidLoader()

class RaidLoader(DataLoader):
    async def batch_load_fn(self, keys):
        return await Raid.batch_loader(keys)
