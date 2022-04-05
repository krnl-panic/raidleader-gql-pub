from ariadne import convert_kwargs_to_snake_case

from api.models import Character


@convert_kwargs_to_snake_case
def listUserCharacters_resolver(obj, info, user_id):
    """

    :param obj: 
    :param info: 
    :param user_id: 

    """
    try:
        characters = [
            character.to_dict() for character in Character.query.filter_by(
                deleted_at=None, user_id=user_id).all()]
        payload = characters
    except Exception as error:
        payload = None
    return payload


@convert_kwargs_to_snake_case
def getCharacter_resolver(obj, info, id):
    """

    :param obj: 
    :param info: 
    :param id: 

    """
    try:
        payload = None
        dataloader = info.context['_character__loader']
        character = dataloader.load(id)
        if character.deleted_at is None:
            payload = character.to_dict()
    except AttributeError:
        payload = None
    return payload
