from api.models import AuctionSession
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listRaidAuctions_resolver(obj, info, raid_id):
    try:
        auction_sessions = [auction_session.to_dict() for auction_session in AuctionSession.query.filter_by(deleted_at=None, raid_id=raid_id)]
        auctions = [auction.to_dict()
                    for auction_session in auction_sessions
                    for auction in auction_session.auctions] 
        payload = auctions
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getAuction_resolver(obj, info, id):
    try:
        payload = None
        auction_session = AuctionSession.query.get(id)
        if auction_session.deleted_at is None:
            payload = auction_session.to_dict()
    except AttributeError:
        payload = None
    return payload