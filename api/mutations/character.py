# mutations.py
from datetime import datetime
from zoneinfo import ZoneInfo
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Character

@convert_kwargs_to_snake_case
def create_character_resolver(obj, info, name, player_class, user_id):
    try:
        character = Character(name=name, player_class=player_class, user_id=user_id)
        db.session.add(character)
        db.session.commit()
        payload = character.to_dict()
    except ValueError:  
        payload = None
    return payload

@convert_kwargs_to_snake_case
def update_character_resolver(obj, info, id, name, player_class, user_id):
    try:
        character = Character.query.filter_by(deleted_at=None, id=id).all()
        if character:
            character.name = name
            character.user_id = user_id
            character.player_class = player_class
        db.session.add(character)
        db.session.commit()
        
        payload = character.to_dict()
    except AttributeError:
        payload = None
    return payload

@convert_kwargs_to_snake_case
def delete_character_resolver(obj, info, id):
    try:        
        character = Character.query.get(id)
        
        if character and character.deleted_at is None:
            character.deleted_at = datetime.now(tz=ZoneInfo('America/New_York'))
            db.session.add(character)
            db.session.commit()
            
        payload = character.to_dict()
    except AttributeError:
        payload = None
    return payload
