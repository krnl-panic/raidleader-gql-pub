# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Auction


@convert_kwargs_to_snake_case
def create_auction_resolver(_, info, raid_id, loot_id):
    """

    :param _:
    :param info:
    :param raid_id:
    :param loot_id:

    """
    try:
        auction = Auction(raid_id=raid_id, loot_id=loot_id)
        db.session.add(auction)
        db.session.commit()
        payload = auction.to_dict()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def update_auction_resolver(_, info, id, raid_id, loot_id):
    """

    :param _:
    :param info:
    :param id:
    :param raid_id:
    :param loot_id:

    """
    try:
        auction = Auction.query.filter_by(deleted_at=None, id=id).all()
        if auction:
            auction.raid_id = raid_id
            auction.loot_id = loot_id
        db.session.add(auction)
        db.session.commit()

        payload = auction.to_dict()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def delete_auction_resolver(_, info, id):
    """

    :param _:
    :param info:
    :param id:

    """
    try:
        auction = Auction.query.get(id)

        if auction and auction.deleted_at is None:
            auction.deleted_at = datetime.now(tz=ZoneInfo("America/New_York"))
            db.session.add(auction)
            db.session.commit()

        payload = auction.to_dict()
    except AttributeError:
        payload = None
    return payload
