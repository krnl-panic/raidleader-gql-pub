from api.models import Loot
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listAuctionLoots_resolver(_, info, auction_id):
    """

    :param _:
    :param info:
    :param auction_id:

    """
    try:
        loots = [
            loot.to_dict()
            for loot in Loot.query.filter_by(
                deleted_at=None, auction_id=auction_id
            ).all()
        ]
        payload = loots
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def listRaidLoots_resolver(_, info, raid_id):
    """

    :param _:
    :param info:
    :param raid_id:

    """
    try:
        loots = [
            loot.to_dict()
            for loot in Loot.query.filter_by(deleted_at=None, raid_id=raid_id).all()
        ]
        payload = loots
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getLoot_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_loot__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
