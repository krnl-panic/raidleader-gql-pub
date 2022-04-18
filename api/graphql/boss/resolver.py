from ariadne import ObjectType

from api.graphql.util import get_loader

boss = ObjectType("Boss")


async def resolve_instance(model_dict, info):
    try:
        loader = get_loader(info, "Instance")
        result = await loader.context_resolver(model_dict)
        payload = result
    except Exception as e:
        print("Caught Exception:", repr(e))
        payload = []
    return payload


async def resolve_items(model_dict, info):
    """

    :param info:

    """

    try:
        loader = get_loader(info, "BossItems")
        result = await loader.resolver(model_dict, info, boss_id=model_dict["id"])
        payload = result
    except Exception as e:
        print("Caught Exception:", repr(e))
        payload = []

    return payload


boss.set_field("items", resolve_items)
boss.set_field("instance", resolve_instance)
