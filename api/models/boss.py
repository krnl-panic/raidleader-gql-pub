from api.database import db


class Boss(db.Model):
    """ """

    __tablename__ = "boss"
    name = db.Column(db.String(128), nullable=False)
    instance_id = db.Column(db.Integer, db.ForeignKey("instance.id"), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "instance_id": self.instance_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
