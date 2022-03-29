from api.models import User
from ariadne import convert_kwargs_to_snake_case

def listUsers_resolver(obj, info):
    try:
        users = [user.to_dict() for user in User.query.filter_by(deleted_at=None).all()]
        payload = users
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getUser_resolver(obj, info, id):
    try:
        payload = None
        dataloader = info.context['_user__loader']
        object = dataloader.load(id)
        if object.deleted_at is None:
            payload = object.to_dict()
    except AttributeError:
        payload = None
    return payload