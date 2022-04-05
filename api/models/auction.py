from aiodataloader import DataLoader

from app import db


class Auction(db.Model):
    """ """
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('auction_session.id'))

    loots = db.relationship('Loot', backref='auction', lazy=True)

    created_at = db.Column(
        db.DateTime(
            timezone=True),
        nullable=False,
        server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(
            timezone=True),
        nullable=False,
        server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))

    def to_dict(self):
        """ """
        return {
            "id": self.id,
            "session": self.session.to_dict(),
            "loots": [loot.to_dict() for loot in self.loots],
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }

    @classmethod
    def loader(self):
        """ """
        return AuctionLoader()


class AuctionLoader(DataLoader):
    """ """

    async def batch_load_fn(self, keys):
        return await Auction.batch_loader(keys)
