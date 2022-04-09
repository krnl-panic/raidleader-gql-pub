from api.models import AuctionSession
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listRaidAuctionSessions_resolver(_, __, raid_id):
    """Returns a list of `AuctionSession` dictionaries.

    :param _: param __:
    :param raid_id: param __:
    :param __:

    """
    try:
        auction_sessions = [
            auction_session.to_dict()
            for auction_session in AuctionSession.query.filter_by(
                deleted_at=None, raid_id=raid_id
            ).all()
        ]
        payload = auction_sessions
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getAuctionSession_resolver(_, info, id):
    """Returns an `AuctionSession` dictionary."""
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_instance__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
