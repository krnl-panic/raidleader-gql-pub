from ariadne import ObjectType
from api.graphql.util import get_loader
from sqlalchemy.exc import DBAPIError

boss = ObjectType("Boss")


async def resolve_items(model_dict, info):
    """

    :param info:

    """

    try:
        loader = get_loader(info, "BossItems")
        result = await loader.resolver(model_dict, info, boss_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


boss.set_field("items", resolve_items)
