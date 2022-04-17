from ariadne import ObjectType, convert_kwargs_to_snake_case

from api.graphql.util import get_loader
from sqlalchemy.exc import DBAPIError

auction_session = ObjectType("AuctionSession")


@convert_kwargs_to_snake_case
async def resolve_auctions(model_dict, info):
    """

    :param model:
    :param info:

    """

    try:
        loader = get_loader(info, "SessionAuctions")
        result = await loader.resolver(model_dict, info, session_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


auction_session.set_field("auctions", resolve_auctions)
