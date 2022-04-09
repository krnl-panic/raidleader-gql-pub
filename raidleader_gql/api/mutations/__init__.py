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

mutation = ObjectType("Mutation")

# Raid Mutations
mutation.set_field("createRaid", create_raid_resolver)
mutation.set_field("updateRaid", update_raid_resolver)
mutation.set_field("deleteRaid", delete_raid_resolver)

# Instance Mutations
mutation.set_field("createInstance", create_instance_resolver)
mutation.set_field("updateInstance", update_instance_resolver)
mutation.set_field("deleteInstance", delete_instance_resolver)

# Boss Mutations
mutation.set_field("createBoss", create_boss_resolver)
mutation.set_field("updateBoss", update_boss_resolver)
mutation.set_field("deleteBoss", delete_boss_resolver)

# Item Mutations
mutation.set_field("createItem", create_item_resolver)
mutation.set_field("updateItem", update_item_resolver)
mutation.set_field("deleteItem", delete_item_resolver)

# Loot Mutations
mutation.set_field("createLoot", create_loot_resolver)
mutation.set_field("updateLoot", update_loot_resolver)
mutation.set_field("deleteLoot", delete_loot_resolver)

# User Mutations
mutation.set_field("createUser", create_user_resolver)
mutation.set_field("updateUser", update_user_resolver)
mutation.set_field("deleteUser", delete_user_resolver)

# Character Mutations
mutation.set_field("createCharacter", create_character_resolver)
mutation.set_field("updateCharacter", update_character_resolver)
mutation.set_field("deleteCharacter", delete_character_resolver)

# AuctionSession Mutations
mutation.set_field("createAuctionSession", create_auction_session_resolver)
mutation.set_field("updateAuctionSession", update_auction_session_resolver)
mutation.set_field("deleteAuctionSession", delete_auction_session_resolver)

# Auction Mutations
mutation.set_field("createAuction", create_auction_resolver)
mutation.set_field("updateAuction", update_auction_resolver)
mutation.set_field("deleteAuction", delete_auction_resolver)
