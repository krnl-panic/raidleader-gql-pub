from ariadne import ObjectType
from api.graphql.util import get_loader
from sqlalchemy.exc import DBAPIError

user = ObjectType("User")


async def resolve_characters(model_dict, info):
    """

    :param info:

    """

    try:
        loader = get_loader(info, "UserCharacters")
        result = await loader.resolver(model_dict, info, user_id=model_dict["id"])
        payload = result
    except DBAPIError as _:
        payload = []

    return payload


user.set_field("characters", resolve_characters)
