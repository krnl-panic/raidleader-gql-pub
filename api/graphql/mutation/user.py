# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import User


@convert_kwargs_to_snake_case
async def create_user_resolver(_, info, discord_id, discord_username):
    """
    Create a new user.
    """
    return await create_resolver(User, info, discord_id=int(discord_id), discord_username=discord_username)


@convert_kwargs_to_snake_case
async def update_user_resolver(_, info, id, discord_id=None, discord_username=None):
    """
    Update an existing user.
    """
    kwargs = {}
    if discord_id is not None:
        kwargs['discord_id'] = int(discord_id)
    if discord_username is not None:
        kwargs['discord_username'] = discord_username

    return await update_resolver(User, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_user_resolver(_, info, id):
    """
    Delete an existing user.
    """
    return await delete_resolver(User, info, model_id=id)
