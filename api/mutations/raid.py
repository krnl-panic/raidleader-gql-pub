# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Raid

@convert_kwargs_to_snake_case
def create_raid_resolver(obj, info, name, start_time, end_time, instance_id):
    try:
        raid = Raid(
            name=name, start_time=start_time, end_time=end_time, instance_id=instance_id
        )
        db.session.add(raid)
        db.session.commit()
        payload = raid.to_dict()
    except ValueError:  
        payload = None
    return payload

@convert_kwargs_to_snake_case
def update_raid_resolver(obj, info, id, name=None, start_time=None, end_time=None):
    try:
        raid = Raid.query.filter_by(deleted_at=None, id=id).all()
        if raid:
            raid.name = name or raid.name
            raid.start_time = start_time or raid.start_time
            raid.end_time = end_time or raid.end_time
            raid.updated_at = datetime.now(tz=ZoneInfo('America/New_York'))
        db.session.add(raid)
        db.session.commit()
        
        payload = raid.to_dict()
    except AttributeError:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def delete_raid_resolver(obj, info, id):
    try:        
        raid = Raid.query.get(id)
        
        if raid and raid.deleted_at is None:
            raid.deleted_at = datetime.now(tz=ZoneInfo('America/New_York'))
            db.session.add(raid)
            db.session.commit()
            
        payload = raid.to_dict()
    except AttributeError:
        payload = None
    return payload
