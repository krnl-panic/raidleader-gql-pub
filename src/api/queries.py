from .models import Raid
from ariadne import convert_kwargs_to_snake_case

def listRaids_resolver(obj, info):
    try:
        raids = [raid.to_dict() for raid in Raid.query.filter_by(deleted_at=None).all()]
        print(raids)
        payload = raids
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getRaid_resolver(obj, info, id):
    try:
        payload = None
        raid = Raid.query.get(id)
        if raid.deleted_at is None:
            payload = raid.to_dict()
    except AttributeError:
        payload = None
    return payload