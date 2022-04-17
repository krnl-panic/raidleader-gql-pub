import functools
from api.context import get_data_loader
from ariadne import convert_kwargs_to_snake_case


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
