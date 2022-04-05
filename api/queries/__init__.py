from ariadne import ObjectType

from .auction import *
from .auction_session import *
from .boss import *
from .character import *
from .instance import *
from .item import *
from .loot import *
from .raid import *
from .user import *

query = ObjectType('Query')

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
