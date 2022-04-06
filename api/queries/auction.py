from api.models import Auction
from ariadne import convert_kwargs_to_snake_case, ObjectType


@convert_kwargs_to_snake_case
def listRaidAuctions_resolver(_, info, raid_id):
    """

    :param _:
    :param info:
    :param raid_id:

    """
    try:
        auction_sessions = [
            auction.to_dict()
            for auction in Auction.query.filter_by(deleted_at=None, raid_id=raid_id)
        ]
        auctions = [
            auction.to_dict()
            for auction_session in auction_sessions
            for auction in auction_session.auctions
        ]
        payload = auctions
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getAuction_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_auction__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
