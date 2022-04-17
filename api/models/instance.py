from api.database import db


class Instance(db.Model):
    """ """

    __tablename__ = "instance"
    name = db.Column(db.String(128), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
