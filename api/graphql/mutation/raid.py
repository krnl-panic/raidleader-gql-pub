# mutation.py

from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Raid
from dateutil.parser import parse


@convert_kwargs_to_snake_case
async def create_raid_resolver(_, info, name, start_time, end_time, instance_id):
    """
    Create a raid
    """
    start = parse(start_time)
    end = parse(end_time)
    return await create_resolver(Raid, info, name=name, start_time=start, end_time=end,
                                 instance_id=int(instance_id))


@convert_kwargs_to_snake_case
async def update_raid_resolver(_, info, id, name=None, start_time=None, end_time=None, instance_id=None):
    """
    Update a raid
    """
    kwargs = {}
    if name:
        kwargs['name'] = name
    if start_time:
        kwargs['start_time'] = parse(start_time)
    if end_time:
        kwargs['end_time'] = parse(end_time)
    if instance_id:
        kwargs['instance_id'] = int(instance_id)
    return await update_resolver(Raid, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_raid_resolver(_, info, id):
    """
    Delete a raid
    """
    return await delete_resolver(Raid, info, model_id=int(id))
