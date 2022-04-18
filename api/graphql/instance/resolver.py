from ariadne import ObjectType
from sqlalchemy.exc import DBAPIError

from api.graphql.util import get_loader

instance = ObjectType("Instance")


async def resolve_bosses(model_dict, info):
    """

    :param info:

    """
    try:
        loader = get_loader(info, "InstanceBosses")
        result = await loader.resolver(model_dict, info, instance_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


instance.set_field("bosses", resolve_bosses)
