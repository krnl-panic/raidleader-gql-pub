# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import AuctionSession


@convert_kwargs_to_snake_case
async def create_auction_session_resolver(_, info, raid_id):
    """
    Create a new auction session.
    """
    return await create_resolver(AuctionSession, info, raid_id=int(raid_id))


@convert_kwargs_to_snake_case
async def update_auction_session_resolver(_, info, id, raid_id=None):
    """
    Update an auction session.
    """
    kwargs = {}
    if raid_id:
        kwargs['raid_id'] = int(raid_id)
    return await update_resolver(AuctionSession, info, model_id=int(id), **kwargs)


@convert_kwargs_to_snake_case
async def delete_auction_session_resolver(_, info, id):
    """
    Delete an auction session.
    """
    return await delete_resolver(AuctionSession, info, model_id=int(id))
