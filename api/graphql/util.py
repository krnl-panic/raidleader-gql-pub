import functools
from typing import Union, Type

from ariadne import convert_kwargs_to_snake_case

from api.context import get_data_loader
from api.database import BaseModel


def loader_resolver(object_type, unbound_method):
    """

    :param object_type: param unbound_method:
    :param unbound_method:

    """

    @functools.wraps(unbound_method)
    @convert_kwargs_to_snake_case
    def _(self, resolve_info, **kwargs):
        """

        :param resolve_info: param **kwargs:
        :param **kwargs:

        """
        loader = get_loader(resolve_info, object_type)
        return unbound_method(loader, self, resolve_info, **kwargs)

    return _


def get_loader(resolve_info, object_type):
    """

    :param resolve_info: param object_type:
    :param object_type:

    """
    return get_data_loader(resolve_info.context, object_type)


async def update_resolver(model_type: Type[BaseModel], resolve_info, model_id: int, **kwargs):
    int_id = int(model_id)
    db_session = resolve_info.context["db_session"]
    payload = None
    try:
        model = await model_type.get(db_session, int_id)
        if model:
            await model.update(db_session, **kwargs)
            await db_session.refresh(model)
            payload = model.to_json()
    except Exception as e:
        print("Caught Exception: ", repr(e))
        payload = None
    return payload


async def delete_resolver(model_type: Type[BaseModel], resolve_info, model_id: Union[int, str]):
    int_id = int(model_id)
    db_session = resolve_info.context["db_session"]
    payload = None
    try:
        model = await model_type.get(db_session, int_id)
        if model:
            await model.delete(db_session)
            await db_session.refresh(model)
            payload = model.to_json()
    except Exception as e:
        print("Caught Exception: ", repr(e))

        payload = None
    return payload


async def create_resolver(model_type: Type[BaseModel], resolve_info, **kwargs):
    db_session = resolve_info.context["db_session"]
    try:
        model = model_type(**kwargs)
        await model.create(db_session)
        await db_session.refresh(model)
        payload = model.to_json()
    except Exception as e:
        print("Caught Exception: ", repr(e))

        payload = None
    return payload
