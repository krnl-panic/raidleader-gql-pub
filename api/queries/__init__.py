from ariadne import ObjectType
from .raid import *
from .instance import *
from .boss import *
from .item import *
from .loot import *
from .user import *
from .character import *
from .auction import *

query = ObjectType('Query')

# Raid Queries
query.set_field("listRaids", listRaids_resolver)
query.set_field("getRaid", getRaid_resolver)

# # Instance Queries
# query.set_field("list", listInstances_resolver)
# query.set_field("get", getInstance_resolver)

# # Boss Queries
# query.set_field("list", listBosses_resolver)
# query.set_field("get", getBoss_resolver)

# # Item Queries
# query.set_field("list", listItems_resolver)
# query.set_field("get", getItem_resolver)

# # Loot Queries
# query.set_field("list", listLoots_resolver)
# query.set_field("get", getLoot_resolver)

# # User Queries
# query.set_field("list", listUsers_resolver)
# query.set_field("get", getUser_resolver)

# # Character Queries
# query.set_field("list", listCharacters_resolver)
# query.set_field("get", getCharacter_resolver)

# # Auction Queries
# query.set_field("list", listAuctions_resolver)
# query.set_field("get", getAuction_resolver)
