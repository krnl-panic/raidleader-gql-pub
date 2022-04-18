from ariadne import ObjectType

from api.graphql.util import get_loader

loot = ObjectType("Loot")


async def item_resolver(model_dict, info):
    try:
        loader = get_loader(info, "Item")
        result = await loader.context_resolver(model_dict)
        payload = result
    except Exception as e:
        print("Caught Exception:", repr(e))
        payload = None
    return payload


async def raid_resolver(model_dict, info):
    try:
        loader = get_loader(info, "Raid")
        result = await loader.context_resolver(model_dict)
        payload = result
    except Exception as e:
        print("Caught Exception:", repr(e))
        payload = None
    return payload


loot.set_field("item", item_resolver)
loot.set_field("raid", raid_resolver)
