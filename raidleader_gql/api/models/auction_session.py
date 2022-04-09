from raidleader_gql import db
from aiodataloader import DataLoader


class AuctionSession(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    raid_id = db.Column(db.Integer, db.ForeignKey("raid.id"))

    auctions = db.relationship("Auction", backref="session", lazy=True)

    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=db.func.now()
    )
    deleted_at = db.Column(db.DateTime(timezone=True))

    def to_dict(self):
        """ """
        return {
            "id": self.id,
            "raid": self.raid.to_dict(),
            "auctions": [auction.to_dict() for auction in self.auctions],
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }

    @staticmethod
    def loader():
        """ """
        return AuctionSessionLoader()


class AuctionSessionLoader(DataLoader):
    """ """

    def batch_load_fn(self, keys):
        return AuctionSession.batch_loader(keys)
