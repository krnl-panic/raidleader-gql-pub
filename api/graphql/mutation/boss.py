# mutation.py
from datetime import datetime
from zoneinfo import ZoneInfo

from api.database import db
from ariadne import convert_kwargs_to_snake_case

from api.models import Boss


@convert_kwargs_to_snake_case
async def create_boss_resolver(_, info, name, instance_id):
    """

    :param _: param info:
    :param name: param instance_id:
    :param info:
    :param instance_id:

    """
    try:
        boss = Boss(name=name, instance_id=instance_id)
        db.session.add(boss)
        db.session.commit()
        payload = boss.to_json()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def update_boss_resolver(_, info, id, name, instance_id):
    """

    :param _: param info:
    :param id: param name:
    :param instance_id:
    :param info:
    :param name:

    """
    try:
        boss = Boss.query.filter_by(deleted_at=None, id=id).all()
        if boss:
            boss.name = name
            boss.instance_id = instance_id
        db.session.add(boss)
        db.session.commit()

        payload = boss.to_json()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def delete_boss_resolver(_, info, id):
    """

    :param _: param info:
    :param id:
    :param info:

    """
    try:
        boss = Boss.query.get(id)

        if boss and boss.deleted_at is None:
            boss.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(boss)
            db.session.commit()

        payload = boss.to_json()
    except AttributeError:
        payload = None
    return payload
