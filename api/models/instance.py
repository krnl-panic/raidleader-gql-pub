from app import db

class Instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    bosses = db.relationship('Boss', backref='instance', lazy=True)

    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bosses": self.bosses,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at
        }