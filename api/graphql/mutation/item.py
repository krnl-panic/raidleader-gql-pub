# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Item


@convert_kwargs_to_snake_case
async def create_item_resolver(_, info, name, boss_id, instance_id, wowhead_url, wow_id):
    """
    Create a new item.
    """
    return await create_resolver(Item, info, name=name, boss_id=int(boss_id), instance_id=int(instance_id),
                                 wowhead_url=wowhead_url, wow_id=int(wow_id))


@convert_kwargs_to_snake_case
async def update_item_resolver(_, info, id, name=None, boss_id=None, instance_id=None, wowhead_url=None):
    """
    Update an existing item.
    """
    kwargs = {}
    if name:
        kwargs['name'] = name
    if boss_id:
        kwargs['boss_id'] = int(boss_id)
    if instance_id:
        kwargs['instance_id'] = int(instance_id)
    if wowhead_url:
        kwargs['wowhead_url'] = wowhead_url
    return await update_resolver(Item, info, model_id=int(id), **kwargs)


@convert_kwargs_to_snake_case
async def delete_item_resolver(_, info, id):
    """
    Delete an existing item.
    """
    return await delete_resolver(Item, info, model_id=int(id))
