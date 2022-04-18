import os

from ariadne import make_executable_schema, load_schema_from_path

from api.graphql.mutation import mutation
from .auction import auction_bindings
from .auction_session import auction_session_bindings
from .boss import boss_bindings
from .character import character_bindings
from .instance import instance_bindings
from .item import item_bindings
from .loot import loot_bindings
from .mutation import mutation
from .query import query
from .raid import raid_bindings
from .user import user_bindings

path = os.path.dirname(__file__)

type_defs = load_schema_from_path(path + "/schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    auction_bindings,
    auction_session_bindings,
    boss_bindings,
    character_bindings,
    instance_bindings,
    item_bindings,
    loot_bindings,
    raid_bindings,
    user_bindings,
)
