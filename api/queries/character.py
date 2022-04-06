from api.models import Character
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listUserCharacters_resolver(_, info, user_id):
    """

    :param _:
    :param info:
    :param user_id:

    """
    try:
        characters = [
            character.to_dict()
            for character in Character.query.filter_by(
                deleted_at=None, user_id=user_id
            ).all()
        ]
        payload = characters
    except Exception:
        payload = None
    return payload


@convert_kwargs_to_snake_case
async def getCharacter_resolver(_, info, id):
    try:
        payload = None
        data_loaders = info.context["data_loaders"]
        dataloader = data_loaders["_character__loader"]
        model = await dataloader.load(id)
        if model.deleted_at is None:
            payload = model.to_dict()
    except AttributeError:
        payload = None
    return payload
