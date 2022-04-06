from ariadne import convert_kwargs_to_snake_case

from api.models import User


def listUsers_resolver(_, info):
    """

    :param _:
    :param info:

    """
    try:
        users = [user.to_dict() for user in User.query.filter_by(deleted_at=None).all()]
        payload = users
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getUser_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_user__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
