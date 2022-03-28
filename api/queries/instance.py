from api.models import Instance
from ariadne import convert_kwargs_to_snake_case

def listInstances_resolver(obj, info):
    try:
        items = [item.to_dict() for item in Instance.query.filter_by(deleted_at=None).all()]
        payload = items
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getInstance_resolver(obj, info, id):
    try:
        payload = None
        item = Instance.query.get(id)
        if item.deleted_at is None:
            payload = item.to_dict()
    except AttributeError:
        payload = None
    return payload