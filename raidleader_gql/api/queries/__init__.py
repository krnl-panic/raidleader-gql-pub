from ariadne import ObjectType
from .raid import listRaids_resolver, getRaid_resolver
from .instance import listInstances_resolver, getInstance_resolver, instance
from .boss import listInstanceBosses_resolver, getBoss_resolver, boss
from .item import listRaidItems_resolver, listBossItems_resolver, getItem_resolver
from .loot import listRaidLoots_resolver, listAuctionLoots_resolver, getLoot_resolver
from .user import listUsers_resolver, getUser_resolver
from .character import listUserCharacters_resolver, getCharacter_resolver
from .auction_session import (
    listRaidAuctionSessions_resolver,
    getAuctionSession_resolver,
)
from .auction import listRaidAuctions_resolver, getAuction_resolver

query = ObjectType("Query")

# Raid Queries
query.set_field("listRaids", listRaids_resolver)
query.set_field("getRaid", getRaid_resolver)

# Instance Queries
query.set_field("listInstances", listInstances_resolver)
query.set_field("getInstance", getInstance_resolver)

# Boss Queries
query.set_field("listInstanceBosses", listInstanceBosses_resolver)
query.set_field("getBoss", getBoss_resolver)

# Item Queries
query.set_field("listBossItems", listBossItems_resolver)
query.set_field("listRaidItems", listRaidItems_resolver)
query.set_field("getItem", getItem_resolver)

# Loot Queries
query.set_field("listAuctionLoots", listAuctionLoots_resolver)
query.set_field("listRaidLoots", listRaidLoots_resolver)
query.set_field("getLoot", getLoot_resolver)

# User Queries
query.set_field("listUsers", listUsers_resolver)
query.set_field("getUser", getUser_resolver)

# Character Queries
query.set_field("listUserCharacters", listUserCharacters_resolver)
# query.set_field("listRaidCharacters", listRaidCharacters_resolver)
query.set_field("getCharacter", getCharacter_resolver)

# AuctionSession Queries
query.set_field("listRaidAuctionSessions", listRaidAuctionSessions_resolver)
query.set_field("getAuctionSession", getAuctionSession_resolver)

# Auction Queries
query.set_field("listRaidAuctions", listRaidAuctions_resolver)
query.set_field("getAuction", getAuction_resolver)
