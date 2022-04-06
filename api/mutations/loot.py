# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Loot


@convert_kwargs_to_snake_case
def create_loot_resolver(_, info, raid_id, item_id):
    """

    :param _:
    :param info:
    :param raid_id:
    :param item_id:

    """
    try:
        loot = Loot(raid_id=raid_id, item_id=item_id)
        db.session.add(loot)
        db.session.commit()
        payload = loot.to_dict()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def update_loot_resolver(_, info, id, raid_id, item_id, auction_id):
    """

    :param _:
    :param info:
    :param id:
    :param raid_id:
    :param item_id:
    :param auction_id:

    """
    try:
        loot = Loot.query.filter_by(deleted_at=None, id=id).all()
        if loot:
            loot.raid_id = raid_id
            loot.item_id = item_id
            loot.auction_id = auction_id
        db.session.add(loot)
        db.session.commit()

        payload = loot.to_dict()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def delete_loot_resolver(_, info, id):
    """

    :param _:
    :param info:
    :param id:

    """
    try:
        loot = Loot.query.get(id)

        if loot and loot.deleted_at is None:
            loot.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(loot)
            db.session.commit()

        payload = loot.to_dict()
    except AttributeError:
        payload = None
    return payload
