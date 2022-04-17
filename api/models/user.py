from api.database import db


class User(db.Model):
    """ """

    __tablename__ = "user"
    discord_id = db.Column(db.BigInteger, nullable=False)
    discord_username = db.Column(db.String, nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "discordId": self.discord_id,
            "discordUsername": self.discord_username,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
