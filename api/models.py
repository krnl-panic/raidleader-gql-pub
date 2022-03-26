from app import db

class Raid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "start_time": self.start_time,
            "created_at": self.created_at
        }