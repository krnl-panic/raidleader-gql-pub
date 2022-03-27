from app import db

class Auction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    raid_id = db.Column(db.Integer, db.ForeignKey('raid.id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    price = db.Column(db.Integer, default=0)

    raid = db.relationship('Raid', backref='auctions', lazy=True)
    winner = db.relationship('Character', backref='won_auctions', lazy=True)
    loots = db.relationship('AuctionLoot', backref='auction', lazy=True)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "raid": self.raid.to_dict(),
            "winner": self.winner.to_dict(),
            "loots": [loot.to_dict() for loot in self.loots],
            "price": self.price,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }