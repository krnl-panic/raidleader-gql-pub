# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Raid


@convert_kwargs_to_snake_case
def create_raid_resolver(_, info, name, start_time, end_time, instance_id):
    """

    :param _: param info:
    :param name: param start_time:
    :param end_time: param instance_id:
    :param info: param start_time:
    :param instance_id:
    :param start_time:

    """
    try:
        raid = Raid(
            name=name, start_time=start_time, end_time=end_time, instance_id=instance_id
        )
        db.session.add(raid)
        db.session.commit()
        payload = raid.to_dict()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def update_raid_resolver(_, info, id, name=None, start_time=None, end_time=None):
    """

    :param _: param info:
    :param id: param name:  (Default value = None)
    :param start_time: Default value = None)
    :param end_time: Default value = None)
    :param info: param name:  (Default value = None)
    :param name:  (Default value = None)

    """
    try:
        raid = Raid.query.filter_by(deleted_at=None, id=id).all()
        if raid:
            raid.name = name or raid.name
            raid.start_time = start_time or raid.start_time
            raid.end_time = end_time or raid.end_time
            raid.updated_at = datetime.now(tz=ZoneInfo("America/New_York"))
        db.session.add(raid)
        db.session.commit()

        payload = raid.to_dict()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def delete_raid_resolver(_, info, id):
    """

    :param _: param info:
    :param id: param info:
    :param info:

    """
    try:
        raid = Raid.query.get(id)

        if raid and raid.deleted_at is None:
            raid.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(raid)
            db.session.commit()

        payload = raid.to_dict()
    except AttributeError:
        payload = None
    return payload
