# mutation.py
from ariadne import convert_kwargs_to_snake_case

from api.graphql.util import create_resolver, update_resolver, delete_resolver
from api.models import Character


@convert_kwargs_to_snake_case
async def create_character_resolver(_, info, name, player_class, user_id):
    """
    Create a new character.
    """
    return await create_resolver(Character, info, name=name, player_class=player_class, user_id=int(user_id))


@convert_kwargs_to_snake_case
async def update_character_resolver(_, info, id, name=None, player_class=None, user_id=None):
    """
    Update a character.
    """
    kwargs = {}
    if name:
        kwargs['name'] = name
    if player_class:
        kwargs['player_class'] = player_class
    if user_id:
        kwargs['user_id'] = int(user_id)
    return await update_resolver(Character, info, model_id=id, **kwargs)


@convert_kwargs_to_snake_case
async def delete_character_resolver(_, info, id):
    """
    Delete a character.
    """
    return await delete_resolver(Character, info, model_id=id)
