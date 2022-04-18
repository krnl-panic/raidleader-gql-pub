from sqlalchemy import Column, String

from api.database import BaseModel


class Instance(BaseModel):
    """ """

    __tablename__ = "instance"
    name = Column(String(128), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
