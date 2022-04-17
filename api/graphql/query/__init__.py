from ariadne import QueryType

from api.data_loaders.auction import AuctionLoader, SessionAuctionsLoader
from api.data_loaders.auction_session import AuctionSessionLoader
from api.data_loaders.boss import BossLoader, InstanceBossesLoader
from api.data_loaders.character import CharacterLoader, UserCharactersLoader
from api.data_loaders.instance import InstanceLoader
from api.data_loaders.item import BossItemsLoader, ItemLoader
from api.data_loaders.loot import AuctionLootsLoader, LootLoader, RaidLootsLoader
from api.data_loaders.raid import RaidLoader
from api.data_loaders.user import UserLoader
from api.graphql.util import loader_resolver
from api.models import (
    Instance as InstanceModel,
    Raid as RaidModel,
    User as UserModel,
)

query = QueryType()


async def list_instances_resolver(_, _info):
    """

    :param _:
    :param _info:

    """
    results = await InstanceModel.query.where(
        InstanceModel.deleted_at is None
    ).gino.all()
    return [instance.to_json() for instance in results]


async def list_raids_resolver(_, _info):
    results = await RaidModel.query.where(RaidModel.deleted_at is None).gino.all()
    return [raid.to_json() for raid in results]


async def list_users_resolver(_, _info):
    """

    :param _:
    :param _info:

    """
    results = await UserModel.query.where(UserModel.deleted_at is None).gino.all()
    return [user.to_json() for user in results]


# Raid Queries
query.set_field("listRaids", list_raids_resolver)
query.set_field("getRaid", loader_resolver("Raid", RaidLoader.resolver))

# Instance Queries
query.set_field("listInstances", list_instances_resolver)
query.set_field("getInstance", loader_resolver("Instance", InstanceLoader.resolver))

# Boss Queries
query.set_field(
    "listInstanceBosses",
    loader_resolver("InstanceBosses", InstanceBossesLoader.resolver),
)
query.set_field("getBoss", loader_resolver("Boss", BossLoader.resolver))

# Item Queries
query.set_field("listBossItems", loader_resolver("BossItems", BossItemsLoader.resolver))
query.set_field("getItem", loader_resolver("Item", ItemLoader.resolver))

# Loot Queries
query.set_field(
    "listAuctionLoots", loader_resolver("AuctionLoots", AuctionLootsLoader.resolver)
)
query.set_field("listRaidLoots", loader_resolver("RaidLoots", RaidLootsLoader.resolver))
query.set_field("getLoot", loader_resolver("Loot", LootLoader.resolver))

# User Queries
query.set_field("listUsers", list_users_resolver)
query.set_field("getUser", loader_resolver("User", UserLoader.resolver))

# Character Queries
query.set_field(
    "listUserCharacters",
    loader_resolver("UserCharacters", UserCharactersLoader.resolver),
)
# query.set_field("listRaidCharacters", listRaidCharacters_resolver)
query.set_field("getCharacter", loader_resolver("Character", CharacterLoader.resolver))

# AuctionSession Queries
query.set_field(
    "listRaidAuctionSessions",
    loader_resolver("SessionAuctions", SessionAuctionsLoader.resolver),
)
query.set_field(
    "getAuctionSession",
    loader_resolver("AuctionSession", AuctionSessionLoader.resolver),
)

# Auction Queries
query.set_field("getAuction", loader_resolver("Auction", AuctionLoader.resolver))
