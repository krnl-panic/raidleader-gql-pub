# context.py
from typing import Dict
from aiodataloader import DataLoader
from api.models import *

def construct_dataloaders() -> Dict[str, DataLoader]:
    dataloaders = {"_instance__loader": Instance.loader()}
    dataloaders = {"_boss__loader": Boss.loader()}
    dataloaders = {"_item__loader": Item.loader()}
    dataloaders = {"_user__loader": User.loader()}
    dataloaders = {"_character__loader": Character.loader()}
    dataloaders = {"_raid__loader": Raid.loader()}
    dataloaders = {"_loot__loader": Loot.loader()}
    dataloaders = {"_auction_session__loader": AuctionSession.loader()}
    dataloaders = {"_auction__loader": Auction.loader()}
    return dataloaders

def get_graphql_context(request) -> Dict[str, Dict[str, DataLoader]]:
    return {"dataloaders": construct_dataloaders(), "request": request}