from api.models import Boss
from ariadne import convert_kwargs_to_snake_case, ObjectType
from api.context import get_data_loader


@convert_kwargs_to_snake_case
def listInstanceBosses_resolver(_, info, instance_id):
    """

    :param _:
    :param info:
    :param instance_id:

    """
    try:
        bosses = [
            boss.to_dict()
            for boss in Boss.query.filter_by(
                deleted_at=None, instance_id=instance_id
            ).all()
        ]
        payload = bosses
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getBoss_resolver(_, info, id):
    try:
        payload = None
        model = await get_data_loader(info.context, "_boss__loader").load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload


boss = ObjectType("Boss")


@boss.field("instance")
async def getInstance_resolver(obj, info, **args):
    try:
        payload = None
    except BaseException:
        AttributeError
    return payload


# @boss.field("items")
# async def getItems_resolver(obj, info, **args):
#     try:
#         payload = None
#     except:
#         AttributeError
#     return payload
