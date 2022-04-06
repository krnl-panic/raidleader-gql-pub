from api.models import Item, Raid
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listBossItems_resolver(_, info, boss_id):
    """

    :param _:
    :param info:
    :param boss_id:

    """
    try:
        items = [
            item.to_dict()
            for item in Item.query.filter_by(deleted_at=None, boss_id=boss_id).all()
        ]
        payload = items
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def listRaidItems_resolver(_, info, raid_id):
    """

    :param _:
    :param info:
    :param raid_id:

    """
    try:
        raid = Raid.query.get(raid_id)
        if raid.deleted_at is None:
            items = [
                item.to_dict()
                for item in Item.query.filter_by(
                    deleted_at=None, instance_id=raid.instance.id
                ).all()
            ]
            payload = items
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getItem_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_item__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
