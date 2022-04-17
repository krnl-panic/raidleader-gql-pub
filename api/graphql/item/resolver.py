from ariadne import ObjectType
from sqlalchemy.exc import DBAPIError

from api.graphql.util import get_loader

item = ObjectType("Item")


async def resolve_boss(model_dict, info):
    """Resolve the boss of the item."""

    try:
        loader = get_loader(info, "Boss")
        result = await loader.load(model_dict["boss_id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


item.set_field("boss", resolve_boss)
