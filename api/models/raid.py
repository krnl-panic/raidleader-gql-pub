from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from api.database import BaseModel


class Raid(BaseModel):
    """ """

    __tablename__ = "raid"
    name = Column(String(128), nullable=False)
    instance_id = Column(Integer, ForeignKey("instance.id"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "instance_id": self.instance_id,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
