from sqlalchemy import Column, Integer, String, ForeignKey

from api.database import BaseModel


class Boss(BaseModel):
    """ """

    __tablename__ = "boss"
    name = Column(String(128), nullable=False)
    instance_id = Column(Integer, ForeignKey("instance.id"), nullable=False)

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
