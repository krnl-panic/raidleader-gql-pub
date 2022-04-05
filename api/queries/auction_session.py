from ariadne import convert_kwargs_to_snake_case

from api.models import AuctionSession


@convert_kwargs_to_snake_case
def listRaidAuctionSessions_resolver(obj, info, raid_id):
    """

    :param obj: 
    :param info: 
    :param raid_id: 

    """
    try:
        auction_sessions = [
            auction_session.to_dict() for auction_session in AuctionSession.query.filter_by(
                deleted_at=None, raid_id=raid_id).all()]
        payload = auction_sessions
    except Exception as error:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getAuctionSession_resolver(obj, info, id):
    """

    :param obj: 
    :param info: 
    :param id: 

    """
    try:
        payload = None
        dataloader = info.context['_auction_session__loader']
        object = dataloader.load(id)
        if object.deleted_at is None:
            payload = object.to_dict()
    except AttributeError:
        payload = None
    return payload
