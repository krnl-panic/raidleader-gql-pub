from ariadne import convert_kwargs_to_snake_case

from api.models import Auction


@convert_kwargs_to_snake_case
def listRaidAuctions_resolver(obj, info, raid_id):
    """

    :param obj: 
    :param info: 
    :param raid_id: 

    """
    try:
        auction_sessions = [
            auction.to_dict() for auction in Auction.query.filter_by(
                deleted_at=None, raid_id=raid_id)]
        auctions = [auction.to_dict()
                    for auction_session in auction_sessions
                    for auction in auction_session.auctions]
        payload = auctions
    except Exception as error:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getAuction_resolver(obj, info, id):
    """

    :param obj: 
    :param info: 
    :param id: 

    """
    try:
        payload = None
        dataloader = info.context['_auction__loader']
        auction = dataloader.load(id)
        if auction.deleted_at is None:
            payload = auction.to_dict()
    except AttributeError:
        payload = None
    return payload
