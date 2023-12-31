from telnetlib import GA
import Classes
import Game
import glob
import json
 
#listy 
enemyList = [];
locationList = [];
eventsList=[];
itemsList=[];
shopList=[];
trapsList=[];
rewardList=[];

#Wrogowie
def ImportEnemy():
    print("Importowanie Wrogów");
    try:
        with open("enemy.txt", "r") as file:
            for line in file:
                name, hitPoints, attack, defence, expDrop = line.strip().split(',');
                enemyList.append(Classes.Enemy(name, int(hitPoints), int(attack), int(defence), int(expDrop)));
                
    except FileNotFoundError:
        print("Plik 'enemy.txt' nie istnieje.");

    return enemyList

def AddEnemyToFile():
    while True:
        name = input("Podaj nazwę wroga: ");
        if name.strip():
            break;
        print("Nie podano wartosci");

    while True:
        hitPoints = input("Podaj ilość punktów życia: ");
        if hitPoints.strip().isdigit():
            break;

    while True:
        attack = input("Podaj wartość ataku: ");
        if attack.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        defence = input("Podaj wartość obrony: ");
        if defence.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        expDrop = input("Podaj ilość doświadczenia za pokonanie: ");
        if expDrop.strip().isdigit():
            break;
        print("Nie podano wartosci");

    with open("enemy.txt", "a") as file:
        file.write(f"{name},{hitPoints},{attack},{defence},{expDrop}\n");

#przedmioty
def ImportItems():
    try:
        with open("items.txt", "r") as file:
            for line in file:
                name, value, hpRegen, attack, defence, hitPoints, itemType = line.strip().split(',');
                itemsList.append(Classes.Item(name, int(value), int(hpRegen), int(attack), int(defence), int(hitPoints), Classes.ItemType[itemType]));
    except FileNotFoundError:
        print("Plik 'items.txt' nie istnieje.");

    return itemsList;

def AddItemToFile():
    while True:
        name = input("Podaj Nawe przedmiotu: ");
        if name.strip():
            break
        print("Nie podano wartosci");
    
    while True:
        value = input("Podaj wartosc przedmiotu: ");
        if value.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    while True:
        hpRegen = input("Podaj ile przedmiot będzie przywracał zdrowia po użyciu: ");
        if hpRegen.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    while True:
        attack = input("Podaj o ile przedmiot będzie zwiekrzal atak: ");
        if attack.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        defence = input("Podaj o ile przedmiot będzie zwiekrzal obrone: ");
        if defence.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        hitPoints = input("Podaj o ile przedmiot będzie zwiekrzal zdrowie: ");
        if hitPoints.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    while True:
        itemType = input("Podaj typ przedmiotu (keyItem, consumable, armor, weapon): ").upper();
        if itemType in Classes.ItemType.__members__:
            break;
        print("Niepoprawny typ przedmiotu. Proszę wybrać z: keyItem, consumable, armor, weapon.");

    with open("items.txt", "a") as file:
        file.write(f"{name},{value},{hpRegen},{attack},{defence},{hitPoints},{itemType}\n");

#Lokacje
def ImportLocation():
    try:
        with open("location.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',');
                name = parts[0];
                enemyID = [];
                eventsID = [];

                for id in parts[1:]:
                    if id.isdigit():
                        if int(id) < 100:
                            enemyID.append(int(id));
                        else:
                            eventsID.append(int(id)-100);

                locationList.append(Classes.Location(name, enemyID, eventsID));
    except FileNotFoundError:
        print("Plik 'location.txt' nie istnieje.");

    return locationList
      
def AddLocationToFile():
     
    enemyID=[];
    eventID=[];
    while True:
        name = input("Podaj nazwę Lokacji: ");
        if name.strip():
          break;
        print("Nie podano wartosci");

    while True:
        enemy = input("Podaj ID wroga (lub wpisz 'exit' aby zakończyć): ");
        if enemy.lower() == 'exit':
            break;
        if enemy.strip().isdigit():
          enemyID.append(int(enemy));
        else:
            print("Nieprawidłowa wartość, wpisz liczbę.");

    while True:    
        event = input("Podaj ID wydarzenia (lub wpisz 'exit' aby zakończyć): ");
        if event.lower() == 'exit':
            break;
        if event.strip().isdigit():
          eventID.append(int(event)+100);
        else:
            print("Nieprawidłowa wartość, wpisz liczbę.");

    with open("location.txt", "a") as file:
        file.write(f"{name},{','.join(map(str, enemyID))},{','.join(map(str, eventID))}\n");

#wydarzenia 
def ImportEvent():
   
    try:
        with open("events.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                description = parts[1]
                eventType = parts[2]
                shopID = int(parts[3]) if parts[3].isdigit() else None
                trapID = int(parts[4]) if parts[4].isdigit() else None
                rewardID = int(parts[4]) if parts[4].isdigit() else None

                event = Classes.Event(name, description, Classes.EventType[eventType], shopID, trapID, rewardID)
                eventsList.append(event)
    except FileNotFoundError:
        print("Plik 'events.txt' nie istnieje.")

    return eventsList

def AddEeventToFile():
    while True:
        name = input("Podaj nazwe wydarzenia: ");
        if name.strip():
            break;
        print("Nie podano wartosci");
    
    while True:
        description = input("Podaj opis: ");
        if description.strip():
            break;
        print("Nie podano wartosci");

    while True:
        eventType = input("Podaj typ przedmiotu (shop, redward, trap): ").upper();
        if eventType in Classes.EventType.__members__:
            break;
        print("Niepoprawny typ przedmiotu. Proszę wybrać z: shop, redward, trap.");
    while True:
        shopID = input("Podaj id sklepu(0 dla braku): ");
        if shopID.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        trapID = input("Podaj id pułapki(0 dla braku): ");
        if trapID.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        rewardID = input("Podaj id Nagrody(0 dla braku): ");
        if rewardID.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    with open("events.txt", "a") as file:
        file.write(f"{name},{description},{eventType},{shopID},{trapID},{rewardID}\n")
#sklep
def ImportShop():
    try:
        with open("shops.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 3:
                    print("Niekompletna linia danych dla sklepu.")
                    continue
                
                name = parts[0]
                entryMessage = parts[1]
                itemsID = [int(id) for id in parts[2:] if id.isdigit()]

                shop = Classes.Shop(name, entryMessage, itemsID)
                shopList.append(shop)
    except FileNotFoundError:
        print("Plik 'shops.txt' nie istnieje.")

    return shopList

def AddShopToFile():
    itemsID=[];
    while True:
        name = input("Podaj nazwę Sklepu: ");
        if name.strip():
          break;
        print("Nie podano wartosci");
    
    while True:
        entryMessage = input("Podaj opis podczas wejścia do sklepu: ");
        if entryMessage.strip():
          break;
        print("Nie podano wartosci");
    while True:
        item = input("Podaj ID przedmiotu (lub wpisz 'exit' aby zakończyć): ");
        if item.lower() == 'exit':
            break;
        if item.strip().isdigit():
          itemsID.append(int(item));
        else:
            print("Nieprawidłowa wartość, wpisz liczbę.");
    with open("shops.txt", "a") as file:
        file.write(f"{name},{entryMessage},{','.join(map(str, itemsID))}\n");
     
#pułapki
def ImportTrap():
    try:
        with open("traps.txt", "r") as file:
            for line in file:
                name, entryMessage, dmg = line.strip().split(',')
                trapsList.append(Classes.Trap(name, entryMessage, int(dmg)))
    except FileNotFoundError:
        print("Plik 'traps.txt' nie istnieje.")

    return trapsList

def AddTrapToFile():
    while True:
        name = input("Podaj nazwe płapki: ");
        if name.strip():
            break;
        print("Nie podano wartosci");

    while True:
        entryMessage = input("Podaj opis podczas wpadania w pułapke: ");
        if entryMessage.strip():
            break;
        print("Nie podano wartosci");
    while True:
        dmg = input("Podaj o ile obrażeń ma zadawać pułapka: ");
        if dmg.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    with open("traps.txt", "a") as file:
        file.write(f"{name},{entryMessage},{dmg}\n")
 
#nagrody
def ImportRedward():
    try:
        with open("redwards.txt", "r") as file:
            for line in file:
                name, entryMessage, gold, itemID = line.strip().split(',')
                rewardList.append(Classes.Redvard(name, entryMessage, int(itemID), int(gold)))
    except FileNotFoundError:
        print("Plik 'redvards.txt' nie istnieje.")

    return rewardList

def AddRedvardToFile():
    while True:
        name = input("Podaj nazwe Nagrody: ");
        if name.strip():
            break;
        print("Nie podano wartosci");

    while True:
        entryMessage = input("Podaj opis podczas znalezienia nagrody: ");
        if entryMessage.strip():
            break;
        print("Nie podano wartosci");
    
    while True:
        gold = input("Podaj o ile złota ma znaleść gracz: ");
        if gold.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    while True:
        itemID = input("Podaj id Przedmiotu, który ma znaleść gracz (0 dla braku): ");
        if itemID.strip().isdigit():
            break;
        print("Nie podano wartosci");
    
    with open("redwards.txt", "a") as file:
        file.write(f"{name},{entryMessage},{gold},{itemID}\n")
#System zapisu i wczytywania
def newGame():
    print("Nowa gra została rozpoczęta!");
    save_files = glob.glob('save*.txt');
    save_number = len(save_files) + 1;
    save_name = f"save{save_number}.txt";

    while True:
        NewName = input("Podaj nazwę postaci: ");
        if NewName.strip():
            break;
        print("Nie podano wartosci");
    Game.chatacterName = NewName;

    while True:
        newDifficulty = input("Wybierz poziom trudności (easy, medium, hard): ").upper();
        if newDifficulty in Classes.Difficulty.__members__:
            break;
        print("Niepoprawny poziom trudności (easy, medium, hard)");  
    Game.difficulty = newDifficulty;
    Game.saveName = save_name;
    saveGame(save_name);
    print(f"Utworzono nowy zapis: {save_name}");
    loadGame(save_name);

def load():
    print("Wybierz zapis do wczytania:");
    save_files = glob.glob('save*.txt');
    if not save_files:
        print("Brak dostępnych zapisów.");
        return;

    for idx, save_file in enumerate(save_files, start=1):
        print(f"{idx}. {save_file}");

    while True:
        choice = input("Wybierz opcję lub wpisz 'exit' aby wyjść: ");
        if choice.lower() == 'exit':
            break;

        if choice.isdigit() and 1 <= int(choice) <= len(save_files):
            selected_save = save_files[int(choice) - 1];
            print(f"Wybrano {selected_save}");
            loadGame(selected_save);
            break;
        else:
            print("Nieprawidłowy wybór");

def saveGame(save_name):
    game_state = {
        "maxHitPoints": Game.maxHitPoints,
        "hitPoints": Game.hitPoints,
        "defence": Game.defence,
        "attack": Game.attak,
        "exp": Game.exp,
        "level": Game.level,
        "difficulty": Game.difficulty,
        "chatacterName": Game.chatacterName,
        "gold": Game.gold,
        "arrmor": Game.arrmorID,
        "weapon": Game.weaponID,
        "itemsId": Game.itemsId,  
        "currentLocationId": Game.currentLocationId,
        "save": Game.saveName
    }

    with open(save_name, "w") as file:
        json.dump(game_state, file);

    print(f"Stan gry zapisano w: {save_name}");

def loadGame(save_name):
    global maxHitPoints,hitPoints,defence,attack,exp,level,difficulty,chatacterName,gold,arrmorID,weaponID,itemsId,currentLocationId,saveName;

    with open(save_name, "r") as file:
        game_state = json.load(file);

    maxHitPoints = game_state["maxHitPoints"];
    hitPoints = game_state["hitPoints"];
    defence = game_state["defence"];
    attack = game_state["attack"];
    exp = game_state["exp"];
    level = game_state["level"];
    difficulty = game_state["difficulty"];
    chatacterName = game_state["chatacterName"];
    gold = game_state["gold"]
    weaponID = game_state["weapon"];
    arrmorID = game_state["arrmor"];
    itemsId = game_state["itemsId"] ;
    currentLocationId = game_state["currentLocationId"];
    saveName = game_state["save"]
    
    Game.LoadStats(maxHitPoints,hitPoints,defence,attack,exp,level,difficulty,chatacterName,gold,arrmorID,weaponID,itemsId,currentLocationId,saveName);
    print(f"Stan gry wczytano z: {save_name}");
    Game.StartGame();