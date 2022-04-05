# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import AuctionSession


@convert_kwargs_to_snake_case
def create_auction_session_resolver(obj, info, raid_id):
    """

    :param obj: 
    :param info: 
    :param raid_id: 

    """
    try:
        auction_session = AuctionSession(raid_id=raid_id)
        db.session.add(auction_session)
        db.session.commit()
        payload = auction_session.to_dict()
    except ValueError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def update_auction_session_resolver(obj, info, id, raid_id):
    """

    :param obj: 
    :param info: 
    :param id: 
    :param raid_id: 

    """
    try:
        auction_session = AuctionSession.query.filter_by(
            deleted_at=None, id=id).all()
        if auction_session:
            auction_session.raid_id = raid_id
        db.session.add(auction_session)
        db.session.commit()

        payload = auction_session.to_dict()
    except AttributeError:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def delete_auction_session_resolver(obj, info, id):
    """

    :param obj: 
    :param info: 
    :param id: 

    """
    try:
        auction_session = AuctionSession.query.get(id)

        if auction_session and auction_session.deleted_at is None:
            auction_session.deleted_at = datetime.now(
                tz=ZoneInfo('America/New_York'))
            db.session.add(auction_session)
            db.session.commit()

        payload = auction_session.to_dict()
    except AttributeError:
        payload = None
    return payload
