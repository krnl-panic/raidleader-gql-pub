# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Loot


@convert_kwargs_to_snake_case
async def create_loot_resolver(_, info, raid_id, item_id, auction_id=None):
    """
    Create a loot.
    """
    kwargs = {"raid_id": int(raid_id), "item_id": int(item_id)}
    if auction_id:
        kwargs["auction_id"] = int(auction_id)
    return await create_resolver(Loot, info, **kwargs)


@convert_kwargs_to_snake_case
async def update_loot_resolver(
    _, info, id, raid_id=None, item_id=None, auction_id=None
):
    """
    Update a loot.
    """
    kwargs = {}
    if raid_id:
        kwargs["raid_id"] = int(raid_id)
    if item_id:
        kwargs["item_id"] = int(item_id)
    if auction_id:
        kwargs["auction_id"] = int(auction_id)
    return await update_resolver(Loot, info, id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_loot_resolver(_, info, id):
    """
    Delete a loot.
    """
    return await delete_resolver(Loot, info, model_id=id)
