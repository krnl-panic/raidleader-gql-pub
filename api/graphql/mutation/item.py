# mutation.py
from datetime import datetime
from zoneinfo import ZoneInfo

from api.database import db
from ariadne import convert_kwargs_to_snake_case

from api.models import Item


@convert_kwargs_to_snake_case
async def create_item_resolver(_, info, name, boss_id, instance_id, wowhead_url):
    """

    :param _: param info:
    :param name: param boss_id:
    :param instance_id: param wowhead_url:
    :param info:
    :param boss_id:
    :param wowhead_url:

    """
    try:
        item = Item(
            name=name, boss_id=boss_id, instance_id=instance_id, wowhead_url=wowhead_url
        )
        db.session.add(item)
        db.session.commit()
        payload = item.to_json()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def update_item_resolver(_, info, id, name, boss_id, instance_id, wowhead_url):
    """

    :param _: param info:
    :param id: param name:
    :param boss_id: param instance_id:
    :param wowhead_url:
    :param info:
    :param name:
    :param instance_id:

    """
    try:
        item = Item.query.filter_by(deleted_at=None, id=id).all()
        if item:
            item.name = name
            item.boss_id = boss_id
            item.instance_id = instance_id
            item.wowhead_url = wowhead_url
        db.session.add(item)
        db.session.commit()

        payload = item.to_json()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def delete_item_resolver(_, info, id):
    """

    :param _: param info:
    :param id:
    :param info:

    """
    try:
        item = Item.query.get(id)

        if item and item.deleted_at is None:
            item.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(item)
            db.session.commit()

        payload = item.to_json()
    except AttributeError:
        payload = None
    return payload
