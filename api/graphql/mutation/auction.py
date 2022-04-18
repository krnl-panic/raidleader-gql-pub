# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Auction


@convert_kwargs_to_snake_case
async def create_auction_resolver(_, info, session_id):
    """
    Create a new auction.
    """
    return await create_resolver(Auction, info, session_id=int(session_id))


@convert_kwargs_to_snake_case
async def update_auction_resolver(_, info, id, session_id=None):
    """
    Update an auction.
    """
    kwargs = {}
    if session_id:
        kwargs['session_id'] = int(session_id)
    return await update_resolver(Auction, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_auction_resolver(_, info, id):
    """
    Delete an auction.
    """
    return await delete_resolver(Auction, info, model_id=id)
