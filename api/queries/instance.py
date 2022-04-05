from ariadne import convert_kwargs_to_snake_case

from api.models import Instance


def listInstances_resolver(obj, info):
    """

    :param obj: 
    :param info: 

    """
    try:
        instances = [
            instance.to_dict() for instance in Instance.query.filter_by(
                deleted_at=None).all()]
        payload = instances
    except Exception as error:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getInstance_resolver(obj, info, id):
    """

    :param obj: 
    :param info: 
    :param id: 

    """
    try:
        payload = None
        dataloader = info.context['_instance__loader']
        object = dataloader.load(id)
        if object.deleted_at is None:
            payload = object.to_dict()
    except AttributeError:
        payload = None
    return payload
