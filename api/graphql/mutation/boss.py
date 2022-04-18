# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Boss


@convert_kwargs_to_snake_case
async def create_boss_resolver(_, info, name, instance_id):
    """
    Create a new boss.
    """
    return await create_resolver(Boss, info, name=name, instance_id=int(instance_id))


@convert_kwargs_to_snake_case
async def update_boss_resolver(_, info, id, name, instance_id):
    """
    Update a boss.
    """
    kwargs = {}
    if name:
        kwargs['name'] = name
    if instance_id:
        kwargs['instance_id'] = int(instance_id)
    return await update_resolver(Boss, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_boss_resolver(_, info, id):
    """
    Delete a boss.
    """
    return await delete_resolver(Boss, info, model_id=id)
