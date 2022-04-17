from api.database import db


class Item(db.Model):
    """ """

    __tablename__ = "item"
    name = db.Column(db.String(128), nullable=False)
    boss_id = db.Column(db.Integer, db.ForeignKey("boss.id"))
    instance_id = db.Column(db.Integer, db.ForeignKey("instance.id"))
    wowhead_url = db.Column(db.String)
    wow_id = db.Column(db.Integer, nullable=False)

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
