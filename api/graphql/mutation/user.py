# mutation.py
from datetime import datetime
from zoneinfo import ZoneInfo

from api.database import db
from ariadne import convert_kwargs_to_snake_case

from api.models import User


@convert_kwargs_to_snake_case
async def create_user_resolver(_, info, discord_id, discord_username):
    """

    :param _: param info:
    :param discord_id: param discord_username:
    :param info:
    :param discord_username:

    """
    try:
        user = User(discord_id, discord_username)
        db.session.add(user)
        db.session.commit()
        payload = user.to_json()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def update_user_resolver(_, info, id, discord_id, discord_username):
    """

    :param _: param info:
    :param id: param discord_id:
    :param discord_username:
    :param info:
    :param discord_id:

    """
    try:
        user = User.query.filter_by(deleted_at=None, id=id).all()
        if user:
            user.discord_id = discord_id
            user.discord_username = discord_username
        db.session.add(user)
        db.session.commit()

        payload = user.to_json()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def delete_user_resolver(_, info, id):
    """

    :param _: param info:
    :param id:
    :param info:

    """
    try:
        user = User.query.get(id)

        if user and user.deleted_at is None:
            user.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(user)
            db.session.commit()

        payload = user.to_json()
    except AttributeError:
        payload = None
    return payload