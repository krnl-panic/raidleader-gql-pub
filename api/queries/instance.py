from api.models import Instance
from ariadne import convert_kwargs_to_snake_case, ObjectType
from api.context import get_data_loader


def listInstances_resolver(_, __):
    """

    :param _:
    :param __:

    """
    try:
        instances = [
            instance.to_dict()
            for instance in Instance.query.filter_by(deleted_at=None).all()
        ]
        payload = instances
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getInstance_resolver(_, info, id):
    try:
        payload = None
        model = await get_data_loader(info.context, "_instance__loader").load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError as error:
        payload = None
    return payload


instance = ObjectType("Instance")


@instance.field("bosses")
async def getBosses_resolver(obj, info, *_):
    try:
        payload = None
    except BaseException:
        AttributeError
    return payload
