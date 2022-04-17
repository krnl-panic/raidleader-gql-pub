from ariadne import ObjectType, convert_kwargs_to_snake_case
from api.graphql.util import get_loader
from sqlalchemy.exc import DBAPIError

raid = ObjectType("Raid")


@convert_kwargs_to_snake_case
async def resolve_loots(model_dict, info):
    """

    :param info:

    """

    try:
        loader = get_loader(info, "RaidLoots")
        result = await loader.resolver(model_dict, info, raid_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


@convert_kwargs_to_snake_case
async def resolve_auctions(model_dict, info):
    """

    :param info:

    """

    try:
        loader = get_loader(info, "RaidAuctionSessions")
        result = await loader.resolver(model_dict, info, raid_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


raid.set_field("loots", resolve_loots)
raid.set_field("auctions", resolve_auctions)
