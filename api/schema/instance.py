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
