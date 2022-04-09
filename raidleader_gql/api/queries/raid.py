from api.models import Raid
from ariadne import convert_kwargs_to_snake_case


def listRaids_resolver(_, info):
    """

    :param _: param info:
    :param info:

    """
    try:
        raids = [raid.to_dict() for raid in Raid.query.filter_by(deleted_at=None).all()]
        payload = raids
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getRaid_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_raid__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
