from api.models import Boss
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listInstanceBosses_resolver(obj, info, instance_id):
    try:
        bosses = [boss.to_dict() for boss in Boss.query.filter_by(deleted_at=None, instance_id=instance_id).all()]
        payload = bosses
    except Exception as error:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def getBoss_resolver(obj, info, id):
    try:
        payload = None
        dataloader = info.context['_boss__loader']
        boss = dataloader.load(id)
        if boss.deleted_at is None:
            payload = boss.to_dict()
    except AttributeError:
        payload = None
    return payload