def print_enemy_list(enemyList):
    if not enemyList:
        print("Lista wrogów jest pusta.")
    else:
        for enemy in enemyList:
            print(f"Wróg: {enemy.name}, HP: {enemy.hitPoints}, Atak: {enemy.attack}, Obrona: {enemy.defence}, EXP Drop: {enemy.expDrop}")

def print_location_list(locationList):
    if not locationList:
        print("Lista lokacji jest pusta.")
    else:
        for location in locationList:
            print(f"Lokacja: {location.name}, ID Wrogów: {location.enemyID}, ID Wydarzeń: {location.eventsID}")

def print_items_list(itemsList):
    if not itemsList:
        print("Lista przedmiotów jest pusta.")
    else:
        for item in itemsList:
            print(f"Przedmiot: {item.name}, Wartość: {item.value}, HP Regen: {item.hpRegen}, Atak: {item.attak}, Obrona: {item.defence}, HP: {item.hitPoints}, ItemType:{item.itemType}")

def print_events_list(eventsList):
    if eventsList:
        for event in eventsList:
            print(f"Wydarzenie: {event.name}, Opis: {event.description}, Typ: {event.eventType}")
    else:
        print("Brak wydarzeń.")

def print_shops_list(shopList):
    if shopList:
        for shop in shopList:
            print(f"Sklep: {shop.name}, Wiadomość powitalna: {shop.entryMessage}, Przedmioty: {shop.itemsID}")
    else:
        print("Brak sklepów.")

def print_traps_list(trapsList):
    if trapsList:
        for trap in trapsList:
            print(f"Pułapka: {trap.name}, Wiadomość: {trap.entryMessage}, Obrażenia: {trap.dmg}")
    else:
        print("Brak pułapek.")

def print_rewards_list(rewardList):
    if rewardList:
        for reward in rewardList:
            print(f"Nagroda: {reward.name}, Wiadomość: {reward.entryMessage}, Przedmiot: {reward.itemID}, Złoto: {reward.gold}")
    else:
        print("Brak nagród.")
