# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Instance


@convert_kwargs_to_snake_case
async def create_instance_resolver(_, info, name):
    """
    Create a new instance.
    """
    return await create_resolver(Instance, info, name=name)


@convert_kwargs_to_snake_case
async def update_instance_resolver(_, info, id, name):
    """
    Update an instance.
    """
    kwargs = {}
    if name:
        kwargs['name'] = name
    return await update_resolver(Instance, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_instance_resolver(_, info, id):
    """
    Delete an instance.
    """
    return await delete_resolver(Instance, info, model_id=id)
