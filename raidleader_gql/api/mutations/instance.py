# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Instance


@convert_kwargs_to_snake_case
def create_instance_resolver(_, info, name):
    """

    :param _: param info:
    :param name: param info:
    :param info:

    """
    try:
        instance = Instance(name=name)
        db.session.add(instance)
        db.session.commit()
        payload = instance.to_dict()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def update_instance_resolver(_, info, id, name):
    """

    :param _: param info:
    :param id: param name:
    :param info: param name:
    :param name:

    """
    try:
        instance = Instance.query.filter_by(deleted_at=None, id=id).all()
        if instance:
            instance.name = name
        db.session.add(instance)
        db.session.commit()

        payload = instance.to_dict()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def delete_instance_resolver(_, info, id):
    """

    :param _: param info:
    :param id: param info:
    :param info:

    """
    try:
        instance = Instance.query.get(id)

        if instance and instance.deleted_at is None:
            instance.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(instance)
            db.session.commit()

        payload = instance.to_dict()
    except AttributeError:
        payload = None
    return payload
