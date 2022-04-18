from ariadne import ObjectType, convert_kwargs_to_snake_case
from sqlalchemy.exc import DBAPIError

from api.graphql.util import get_loader

auction = ObjectType("Auction")


@convert_kwargs_to_snake_case
async def resolve_session(model_dict, info):
    try:
        loader = get_loader(info, "AuctionSession")
        result = await loader.context_resolver(model_dict)
        payload = result
    except Exception as e:
        print("Caught Exception: ", repr(e))
        payload = []
    return payload


@convert_kwargs_to_snake_case
async def resolve_loots(model_dict, info):
    """

    :param model:
    :param info:

    """

    try:
        loader = get_loader(info, "AuctionLoots")
        result = await loader.resolver(model_dict, info, auction_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


auction.set_field("loots", resolve_loots)
auction.set_field("session", resolve_session)
