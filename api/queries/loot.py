from api.models import Loot
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listAuctionLoots_resolver(obj, info, auction_id):
    try:
        loots = [loot.to_dict() for loot in Loot.query.filter_by(deleted_at=None, auction_id=auction_id).all()]
        payload = loots
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def listRaidLoots_resolver(obj, info, raid_id):
    try:
        loots = [loot.to_dict() for loot in Loot.query.filter_by(deleted_at=None, raid_id=raid_id).all()]
        payload = loots
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getLoot_resolver(obj, info, id):
    try:
        payload = None
        loot = Loot.query.get(id)
        if loot.deleted_at is None:
            payload = loot.to_dict()
    except AttributeError:
        payload = None
    return payload