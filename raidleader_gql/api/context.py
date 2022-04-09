# context.py
"""
Collection of helper functions to create a context linking
model data loaders to a GraphQL request.
"""
from typing import Dict
from aiodataloader import DataLoader
from api.models import (
    Instance,
    Boss,
    Item,
    User,
    Character,
    Raid,
    Loot,
    AuctionSession,
    Auction,
)


def construct_data_loaders() -> Dict[str, DataLoader]:
    """Construct `DataLoader` objects for each model."""
    data_loaders = {
        "_instance__loader": Instance.loader(),
        "_boss__loader": Boss.loader(),
        "_item__loader": Item.loader(),
        "_user__loader": User.loader(),
        "_character__loader": Character.loader(),
        "_raid__loader": Raid.loader(),
        "_loot__loader": Loot.loader(),
        "_auction_session__loader": AuctionSession.loader(),
        "_auction__loader": Auction.loader(),
    }
    return data_loaders


def get_graphql_context(request) -> Dict[str, Dict[str, DataLoader]]:
    """Returns the request and dataloader context for a GraphQL request.

    :param request:

    """
    return {"data_loaders": construct_data_loaders(), "request": request}


def get_data_loader(context, key):
    """

    :param context: param key:
    :param key:

    """
    data_loaders = context["data_loaders"]
    return data_loaders[key]
