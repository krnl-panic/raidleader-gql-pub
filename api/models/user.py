from sqlalchemy import Column, String, BigInteger

from api.database import BaseModel


class User(BaseModel):
    """ """

    __tablename__ = "user"
    discord_id = Column(BigInteger, nullable=False)
    discord_username = Column(String, nullable=False)

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
