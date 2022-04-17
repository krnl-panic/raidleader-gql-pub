# mutation.py
from datetime import datetime
from zoneinfo import ZoneInfo

from api.database import db
from ariadne import convert_kwargs_to_snake_case

from api.models import Instance


@convert_kwargs_to_snake_case
async def create_instance_resolver(_, info, name):
    """

    :param _: param info:
    :param name:
    :param info:

    """
    try:
        instance = Instance(name=name)
        db.session.add(instance)
        db.session.commit()
        payload = instance.to_json()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def update_instance_resolver(_, info, id, name):
    """

    :param _: param info:
    :param id: param name:
    :param info:
    :param name:

    """
    try:
        instance = Instance.query.filter_by(deleted_at=None, id=id).all()
        if instance:
            instance.name = name
        db.session.add(instance)
        db.session.commit()

        payload = instance.to_json()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def delete_instance_resolver(_, info, id):
    """

    :param _: param info:
    :param id:
    :param info:

    """
    try:
        instance = Instance.query.get(id)

        if instance and instance.deleted_at is None:
            instance.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(instance)
            db.session.commit()

        payload = instance.to_json()
    except AttributeError:
        payload = None
    return payload
