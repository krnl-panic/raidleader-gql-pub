import graphene as gql


class AuctionSession(gql.ObjectType):
    """ """

    id = gql.ID()
    auctions = gql.List(lambda: Auction)


class Auction(gql.ObjectType):
    """ """

    id = gql.ID()
    session = gql.Field(lambda: AuctionSession)
    loot = gql.Field(lambda: Loot)
    winner = gql.Field(lambda: Character)
    price = gql.Int()


class Raid(gql.ObjectType):
    """ """

    id = gql.ID()
    name = gql.String()
    instance = gql.Field(lambda: Instance)
    start_time = gql.DateTime()
    end_time = gql.DateTime()


class PlayerClass(gql.Enum):
    """ """

    DRUID = "druid"
    MAGE = "mage"
    HUNTER = "hunter"
    ROGUE = "rogue"
    SHAMAN = "shaman"
    PALADIN = "paladin"
    PRIEST = "priest"
    WARRIOR = "warrior"
    WARLOCK = "warlock"
    DEATHKNIGHT = "deathknight"


class Character(gql.ObjectType):
    """ """

    id = gql.ID()
    name = gql.String()
    user = gql.Field(lambda: User)
    player_class = gql.Field(lambda: PlayerClass)


class User(gql.ObjectType):
    """ """

    id = gql.ID()
    characters = gql.List(lambda: Character)


class Loot(gql.ObjectType):
    """ """

    id = gql.ID()
    raid = gql.Field(lambda: Raid)
    item = gql.Field(lambda: Item)


class Item(gql.ObjectType):
    """ """

    id = gql.ID()
    name = gql.String()
    boss = gql.Field(lambda: Boss)
    wowhead_url = gql.String()
    instance = gql.Field(lambda: Instance)


class Boss(gql.ObjectType):
    """ """

    id = gql.ID()
    name = gql.String()
    items = gql.List(lambda: Item)


class Instance(gql.ObjectType):
    """ """

    id = gql.ID()
    name = gql.String()
    bosses = gql.List(lambda: Boss)


class Query(gql.ObjectType):
    """Graphene Query Class"""

    list_instances = gql.List(Instance)
    get_instance = gql.Field(Instance, id=gql.ID())

    list_raids = gql.List(Raid)
    get_raid = gql.Field(Raid, id=gql.ID())

    list_instance_bosses = gql.List(Boss, instance_id=gql.ID())
    get_boss = gql.Field(Boss, id=gql.ID())

    list_boss_items = gql.List(Item, boss_id=gql.ID())
    list_raid_items = gql.List(Item, raid_id=gql.ID())
    get_item = gql.Field(Item, id=gql.ID())

    list_auction_loots = gql.List(Loot, auction_id=gql.ID())
    list_raid_loots = gql.List(Loot, raid_id=gql.ID())
    get_loot = gql.Field(Loot, id=gql.ID())

    list_users = gql.List(User)
    get_user = gql.Field(User, id=gql.ID())

    list_user_characters = gql.List(Character, user_id=gql.ID())
    get_character = gql.Field(Character, id=gql.ID())

    list_raid_auction_sessions = gql.List(AuctionSession, raid_id=gql.ID())
    get_auction_session = gql.Field(AuctionSession, id=gql.ID())

    list_session_auctions = gql.List(Auction, session_id=gql.ID())
    get_auction = gql.Field(Auction, id=gql.ID())


schema = gql.Schema(query=Query)
