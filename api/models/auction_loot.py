from app import db

class AuctionLoot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    auction_id = db.Column(db.Integer, db.ForeignKey('auction.id'))
    loot_id = db.Column(db.Integer, db.ForeignKey('loot.id'))

    loot = db.relationship('Loot', lazy=True)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "auction": self.auction.to_dict(),
            "loot": self.loot.to_dict(),
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }