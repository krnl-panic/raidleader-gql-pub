# context.py
"""
Collection of helper functions to create a context linking
model data loaders to a GraphQL request.
"""
from typing import Dict

from aiodataloader import DataLoader
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

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


def construct_data_loaders(db_session: AsyncSession) -> Dict[str, DataLoader]:
    """Construct `DataLoader` objects for each model."""
    data_loaders = {
        "Instance": InstanceLoader(db_session),
        "InstanceBosses": InstanceBossesLoader(db_session),
        "Boss": BossLoader(db_session),
        "BossItems": BossItemsLoader(db_session),
        "Item": ItemLoader(db_session),
        "User": UserLoader(db_session),
        "UserCharacters": UserCharactersLoader(db_session),
        "Character": CharacterLoader(db_session),
        "Raid": RaidLoader(db_session),
        "RaidLoots": RaidLootsLoader(db_session),
        "RaidAuctionSessions": RaidAuctionSessionsLoader(db_session),
        "Loot": LootLoader(db_session),
        "AuctionSession": AuctionSessionLoader(db_session),
        "SessionAuctions": SessionAuctionsLoader(db_session),
        "Auction": AuctionLoader(db_session),
        "AuctionLoots": AuctionLootsLoader(db_session),
    }
    return data_loaders


def get_graphql_context(request: Request, session: AsyncSession) -> Dict[str, any]:
    """Returns the request and dataloader context for a GraphQL request.

    :param request:

    """
    return {"data_loaders": construct_data_loaders(session), "request": request, "db_session": session}


def get_data_loader(context, key):
    """

    :param context: param key:
    :param key:

    """
    data_loaders = context["data_loaders"]
    return data_loaders[key]
