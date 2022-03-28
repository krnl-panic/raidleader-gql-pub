from api.models import Item, Raid
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listBossItems_resolver(obj, info, boss_id):
    try:
        items = [item.to_dict() for item in Item.query.filter_by(deleted_at=None, boss_id=boss_id).all()]
        payload = items
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def listRaidItems_resolver(obj, info, raid_id):
    try:
        raid = Raid.query.get(raid_id)
        if raid.deleted_at is None:
            items = [
                item.to_dict() for item in Item.query.filter_by(deleted_at=None, instance_id=raid.instance.id).all()]
            payload = items
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getItem_resolver(obj, info, id):
    try:
        payload = None
        item = Item.query.get(id)
        if item.deleted_at is None:
            payload = item.to_dict()
    except AttributeError:
        payload = None
    return payload