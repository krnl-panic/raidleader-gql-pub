# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Raid

@convert_kwargs_to_snake_case
def create_raid_resolver(obj, info, title, start_time):
    try:
        today = datetime.now(tz=ZoneInfo('America/New_York'))
        raid = Raid(
            title=title, start_time=start_time, created_at=today
        )
        db.session.add(raid)
        db.session.commit()
        payload = {
            "success": True,
            "raid": raid.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy."]
        }
    return payload

@convert_kwargs_to_snake_case
def update_raid_resolver(obj, info, id, title, start_time):
    try:
        raid = Raid.query.get(id)
        if raid:
            raid.title = title
            raid.start_time = start_time
        db.session.add(raid)
        db.session.commit()
        payload = {
            "success": True,
            "raid": raid.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Item matching id {id} not found."]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_raid_resolver(obj, info, id):
    try:
        raid = Raid.query.get(id)
        db.session.delete(raid)
        db.session.commit()
        payload = {"success": True, "post": raid.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found."]
        }
    return payload
