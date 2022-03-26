from .models import Raid
from ariadne import convert_kwargs_to_snake_case

def listRaids_resolver(obj, info):
    try:
        raids = [raid.to_dict() for raid in Raid.query.all()]
        print(raids)
        payload = {
            "success": True,
            "raids": raids
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getRaid_resolver(obj, info, id):
    try:
        raid = Raid.query.get(id)
        payload = {
            "success": True,
            "raid": raid.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Raid item matching {id} not found"]
        }
    return payload