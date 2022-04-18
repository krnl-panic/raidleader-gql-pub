from sqlalchemy import Column, Integer, String, ForeignKey

from api.database import BaseModel


class Item(BaseModel):
    """ """

    __tablename__ = "item"
    name = Column(String(128), nullable=False)
    boss_id = Column(Integer, ForeignKey("boss.id"))
    instance_id = Column(Integer, ForeignKey("instance.id"))
    wowhead_url = Column(String)
    wow_id = Column(Integer, nullable=False)

    def to_json(self):
        """ """
        return {
            "id": self.id,
            "name": self.name,
            "boss_id": self.boss_id,
            "instance_id": self.instance_id,
            "wowheadUrl": self.wowhead_url,
            "wowId": self.wow_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "deletedAt": self.deleted_at,
        }
