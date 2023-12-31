#Classes.py
from enum import Enum

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD =  "hard"

class Enemy:
    def __init__(self, name, hitPoints, attack, defence, expDrop):
        self.name = name;
        self.hitPoints = hitPoints;
        self.attack = attack;
        self.defence = defence;
        self.expDrop = expDrop;

class ItemType(Enum):
    KEY_ITEM = "keyItem"
    CONSUMABLE = "consumable"
    ARMOR = "armor"
    WEAPON = "weapon"

class Item:
    def __init__(self,name,value,hpRegen,attak, defence, hitPoints, itemType):
        self.name = name;
        self.value = value;
        self.hpRegen = hpRegen;
        self.attak =attak;
        self.defence = defence;
        self.hitPoints = hitPoints;
        self.itemType = itemType;
        

class Location:
    def __init__(self, name, enemyID, eventsID):
        self.name = name;
        self.enemyID = enemyID;
        self.eventsID = eventsID;

class EventType(Enum):
    SHOP = "shop"
    REDWARD = "redward"
    TRAP = "trap"

class Event:
    def __init__(self, name, description, eventType,shopID, trapID, rewardID):
        self.name = name;
        self.description = description;
        self.eventType = eventType;
        self.shopID = shopID;
        self.trapID = trapID;
        self.rewardID = rewardID;

class Shop:
    def __init__(self,name, entryMessage, itemsID):
        self.name =name;
        self.entryMessage = entryMessage;
        self.itemsID = itemsID;

class Trap:
     def __init__(self,name, entryMessage, dmg):
        self.name =name;
        self.entryMessage = entryMessage;
        self.dmg = dmg;

class Redvard:
     def __init__(self,name, entryMessage, itemID, gold):
        self.name =name;
        self.entryMessage = entryMessage;
        self.itemID = itemID;
        self.gold = gold;



