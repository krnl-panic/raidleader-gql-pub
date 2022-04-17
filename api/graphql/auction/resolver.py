from ariadne import ObjectType, convert_kwargs_to_snake_case
from api.graphql.util import get_loader
from sqlalchemy.exc import DBAPIError

auction = ObjectType("Auction")


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
