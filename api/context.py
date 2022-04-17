# context.py
"""
Collection of helper functions to create a context linking
model data loaders to a GraphQL request.
"""
from typing import Dict
from api.data_loaders import (
    AuctionLoader,
    AuctionSessionLoader,
    BossLoader,
    CharacterLoader,
    InstanceLoader,
    ItemLoader,
    LootLoader,
    RaidLoader,
    UserLoader,
    InstanceBossesLoader,
    BossItemsLoader,
    RaidLootsLoader,
    AuctionLootsLoader,
    SessionAuctionsLoader,
    RaidAuctionSessionsLoader,
    UserCharactersLoader,
)
from aiodataloader import DataLoader


def construct_data_loaders() -> Dict[str, DataLoader]:
    """Construct `DataLoader` objects for each model."""
    data_loaders = {
        "Instance": InstanceLoader(),
        "InstanceBosses": InstanceBossesLoader(),
        "Boss": BossLoader(),
        "BossItems": BossItemsLoader(),
        "Item": ItemLoader(),
        "User": UserLoader(),
        "UserCharacters": UserCharactersLoader(),
        "Character": CharacterLoader(),
        "Raid": RaidLoader(),
        "RaidLoots": RaidLootsLoader(),
        "RaidAuctionSessions": RaidAuctionSessionsLoader(),
        "Loot": LootLoader(),
        "AuctionSession": AuctionSessionLoader(),
        "SessionAuctions": SessionAuctionsLoader(),
        "Auction": AuctionLoader(),
        "AuctionLoots": AuctionLootsLoader(),
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
