from api.models import Raid
from ariadne import convert_kwargs_to_snake_case

def listRaids_resolver(obj, info):
    try:
        raids = [raid.to_dict() for raid in Raid.query.filter_by(deleted_at=None).all()]
        payload = raids
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getRaid_resolver(obj, info, id):
    try:
        payload = None
        dataloader = info.context['_raid__loader']
        object = dataloader.load(id)
        if object.deleted_at is None:
            payload = object.to_dict()
    except AttributeError:
        payload = None
    return payload