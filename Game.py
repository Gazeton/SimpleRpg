import time
import Classes
import Data
import Debug
import BattleSystem
import random
import sys

maxHitPoints = 10;
hitPoints = 10;
attak = 1;
defence = 0;
exp = 0;
level = 1;

difficulty = Classes.Difficulty.EASY;
chatacterName = "empty";
gold = 0;

arrmorID = 0;
weaponID = 0;

itemsId: int = [5,2,3,9];

currentLocationId = 0; 

saveName = "save1"

def StartGame():
    print(f"grasz jako {chatacterName} na poziomie {level}")
    ImportData();
    PlayerChoice();

def LoadStats(new_maxHitPoints, new_hitPoints, new_defence, new_attack, new_exp, new_level, new_difficulty, new_chatacterName, new_gold,new_arrmorID,new_weaponID, new_itemsId, new_currentLocationId,new_saveName):
    global maxHitPoints,hitPoints,attak,defence,exp,level,difficulty,chatacterName,gold,arrmorID,weaponID,itemsId,currentLocationId,saveName;

    maxHitPoints = new_maxHitPoints;
    hitPoints = new_hitPoints;
    defence = new_defence;
    attak = new_attack;
    exp = new_exp;
    level = new_level;
    chatacterName =new_chatacterName;
    gold = new_gold;
    itemsId = new_itemsId;
    currentLocationId = new_currentLocationId;
    difficulty = new_difficulty;
    weaponID = new_weaponID;
    arrmorID = new_arrmorID;
    saveName = new_saveName;

def PlayerChoice():
    time.sleep(1.0)
    while True:
        if currentLocationId == 0:
            PlayerChoiceInTown();
        else:
            PlayerChoiceInAdventure();

def PlayerChoiceInAdventure():
    print("Wybierz akcję:")
    print("1. Powrót do miasta")
    print("2. Pójście dalej")
    print("3. Otworzenie ekwipunku")

    choice = input("Twój wybór: ")
  
    if choice == "1":
        ReturnToCity()
    elif choice == "2":
        ContinueJourney()
    elif choice == "3":
        OpenInventory()
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
        PlayerChoiceInAdventure()

def PlayerChoiceInTown():
    global saveName,weaponID,arrmorID,maxHitPoints,hitPoints
    print("Wybierz akcję:")
    print("1. Przygoda")
    print("2. Sklep")
    print("3. Odpoczynek")
    print("4. Otworzenie ekwipunku")
    print("5. zapisz gre")
    print("6. wyjdź z gry")

    choice = input("Twój wybór: ")

    if choice == '1':
        SelectLocation();
    elif choice == "2":
        OpenShop(0)
    elif choice == "3":
        print("poszedłeś do domu i wyleczyłeś rany twoje zdrowie wraca do normy")
        weapon = Data.itemsList[weaponID];
        arrmor = Data.itemsList[arrmorID];
        totalMaxHp = maxHitPoints + weapon.hitPoints + arrmor.hitPoints;
        hitPoints = totalMaxHp
    elif choice == "4":
        OpenInventory()
    elif choice == "5":
       Data.saveGame(saveName)
    elif choice == "6":
        sys.exit();
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
        PlayerChoice()

def SelectLocation():
    global currentLocationId
    if Data.locationList:
        print("Dostępne lokacje:")
        for index, location in enumerate(Data.locationList):
            print(f"{index}: {location.name}")

        while True:
            choice = input("Wybierz numer lokacji: ")
            if choice.isdigit() and int(choice) < len(Data.locationList):
                currentLocationId = int(choice)
                print(f"Wybrano lokację: {Data.locationList[currentLocationId].name}")
                print(currentLocationId)
                break

            else:
                print("Nieprawidłowy wybór. Proszę wybrać poprawny numer lokacji.")
    else:
        print("Brak dostępnych lokacji.")

def ReturnToCity():
    global currentLocationId
    print("wracasz do miasta")
    currentLocationId = 0

def OpenShop(ShopID):
    global gold, itemsId ,priceMultiplier 

    shop = Data.shopList[ShopID]
    print(f"Witaj w sklepie: {shop.name}")
    print(shop.entryMessage)

    # Ustalanie mnożnika cen
    if difficulty == Classes.Difficulty.EASY:
        priceMultiplier = 0.75
    elif difficulty == Classes.Difficulty.MEDIUM:
        priceMultiplier = 1.00
    elif difficulty == Classes.Difficulty.HARD:
        priceMultiplier = 1.50
    else:
        priceMultiplier = 1.00

    while True:
        print("\n1. Kup przedmiot")
        print("2. Sprzedaj przedmiot")
        print("3. Wyjdź ze sklepu")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            # Kupowanie przedmiotu
            print(f"Posiadasz {gold} złota Dostępne przedmioty do kupienia:")
            for itemId in shop.itemsID:
                item = Data.itemsList[itemId]
                print(f"{itemId} - {item.name} | Cena: {int(item.value * priceMultiplier)} złota")

            item_to_buy = input("Wpisz ID przedmiotu do kupienia lub 'exit', aby wyjść: ")
            if item_to_buy.isdigit() and int(item_to_buy) in shop.itemsID:
                item_to_buy = int(item_to_buy)
                item_price = int(Data.itemsList[item_to_buy].value * priceMultiplier)
                if gold >= item_price:
                    gold -= item_price
                    itemsId.append(item_to_buy)
                    print(f"Kupiono {Data.itemsList[item_to_buy].name} za {item_price} złota. Pozostało złota: {gold}")
                else:
                    print("Nie masz wystarczająco złota.")
            elif item_to_buy == 'exit':
                continue
            else:
                print("Nieprawidłowy wybór przedmiotu.")

        elif choice == '2':
            # Sprzedawanie przedmiotu
            print("Twoje przedmioty do sprzedania:")
            for itemId in itemsId:
                item = Data.itemsList[itemId]
                print(f"{itemId} - {item.name} | Cena sprzedaży: {int(item.value * 0.5)} złota")

            item_to_sell = input("Wpisz ID przedmiotu do sprzedania lub 'exit', aby wyjść: ")
            if item_to_sell.isdigit() and int(item_to_sell) in itemsId:
                item_to_sell = int(item_to_sell)
                sell_price = int(Data.itemsList[item_to_sell].value * 0.5)
                gold += sell_price
                itemsId.remove(item_to_sell)
                print(f"Sprzedano {Data.itemsList[item_to_sell].name} za {sell_price} złota. Posiadasz teraz złota: {gold}")
            elif item_to_sell == 'exit':
                continue
            else:
                print("Nieprawidłowy wybór przedmiotu.")

        elif choice == '3':
            print("Opuszczasz sklep.")
            break
        else:
            print("Nieprawidłowy wybór.")

def ContinueJourney():
    print("Idziesz dalej.")
    currentLocation = Data.locationList[currentLocationId]

    if not currentLocation.enemyID and not currentLocation.eventsID:
        print("Nie ma wrogów ani wydarzeń w tej lokacji.")
        return

    if random.random() < 0.75 and currentLocation.enemyID:  
        enemyId = random.choice(currentLocation.enemyID)
        enemy = Data.enemyList[enemyId]
        print(f"Walczysz z wrogiem: {enemy.name}")
        BattleSystem.BattleStart(enemyId)

    elif currentLocation.eventsID:  
        eventId = random.choice(currentLocation.eventsID)
        event = Data.eventsList[eventId]
        print(f"Wydarzenie: {event.name}, \n {event.description}")

        # Dodać logikę obsługi wydarzenia
    else:
        print("Nie ma dostępnych wrogów ani wydarzeń w tej lokacji.")
#wydarzenia
def ActivateEvent(EventId):
    event = Data.eventList[EventId]
    global hitPoints,gold
    print(f"Wydarzenie: {event.name}, Opis: {event.description}")

    if event.eventType == Classes.EventType.SHOP:
        OpenShop(event.shopID)

    elif event.eventType == Classes.EventType.REDWARD:
        reward = Data.rewardList[event.rewardID]  # Uzyskaj obiekt nagrody
        print(f"Aktywowano nagrodę: {reward.name}")
        print(reward.entryMessage)

        if reward.itemID is not None:
            itemsId.append(reward.itemID)  # Dodaj ID przedmiotu do ekwipunku gracza
            print(f"Otrzymałeś przedmiot: {Data.itemsList[reward.itemID].name}")

        gold += reward.gold  # Dodaj złoto do ekwipunku gracza
        print(f"Otrzymałeś {reward.gold} złota. Obecnie masz {gold} złota.")

    elif event.eventType == Classes.EventType.TRAP:
        trap = Data.trapList[event.trapID]  # Uzyskaj obiekt pułapki
        print(f"Aktywowano pułapkę: {trap.name}")
        print(trap.entryMessage)
    
        hitPoints -= trap.dmg  # Odejmij obrażenia od punktów życia
        if hitPoints <= 0:
            print("umierasz")
            PlayerDead();
        else:
            print(f"Otrzymałeś {trap.dmg} obrażeń. Pozostało Ci {hitPoints} punktów życia.")

    else:
        print("Nieznany typ wydarzenia.")  

#Zrządzanie przedmiotami 
def UseConsumable():
    global hitPoints
    print("Dostępne przedmioty leczące w twoim ekwipunku:")
    availableConsumables = {}
    if itemsId:
        for thisItemId in itemsId:
            item = Data.itemsList[thisItemId]
            if item.itemType == Classes.ItemType.CONSUMABLE:
                print(f"{thisItemId} - Name: {item.name} | Regeneruje: {item.hpRegen}")
                availableConsumables[thisItemId] = item

        if availableConsumables:
            newConsumableID = input("Wpisz ID przedmiotu konsumowalnego, który chcesz użyć: ")
            if newConsumableID.isdigit() and int(newConsumableID) in availableConsumables:
                consumableID = int(newConsumableID)
                print(f"Wybrano do użycia: {availableConsumables[consumableID].name}")
                hitPoints += availableConsumables[consumableID].hpRegen
                weapon = Data.itemsList[weaponID];
                arrmor = Data.itemsList[arrmorID];
                if hitPoints> maxHitPoints + weapon.hitPoints + arrmor.hitPoints:
                    hitPoints=maxHitPoints + weapon.hitPoints + arrmor.hitPoints
                itemsId.remove(consumableID)
            else:
                print("Niepoprawne ID przedmiotu konsumowalnego.")
        else:
            print("Nie posiadasz żadnych przedmiotów konsumowalnych.")
    else:
        print("Nie posiadasz żadnych przedmiotów konsumowalnych.")

def ShowOpenInventory():
    print("1. Sprawdź statystyki postaci.");
    print("2. Sprawdź wyposarzenie postaci.");
    print("3. Zmień Broń")
    print("4. Zmień Zbroje")
    print("5. Sprawdź wszystkie przedmioty.");
    print("6. użyj przedmiotu leczącego");

def OpenInventory():   
    while True:
        ShowOpenInventory();
        sub_choice = input("Wybierz opcję (1-5) lub 'exit' aby wrócić do poprzedniego menu: ");
        if sub_choice == '1':
            ShowStats();      
        elif sub_choice == '2':
            ShowEquipment();
        elif sub_choice == '3':
            ChangeWeapon();
        elif sub_choice == '4':
            ChangeArmor();
        elif sub_choice == '5':
            printItemsInInventory();
        elif sub_choice == '6':
            UseConsumable();
        elif sub_choice.lower() == 'exit':
           break;
        else:
            print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 5");

def printItemsInInventory():
    if itemsId:
        for thisItemId in itemsId:
            item = Data.itemsList[thisItemId];
            print(f"Name: {item.name}");
            print(f"Value: {item.value}");
            print(f"HP Regeneration: {item.hpRegen}");
            print(f"Attack: {item.attak}");
            print(f"Defence: {item.defence}");
            print(f"Hit Points: {item.hitPoints}");
            print(f"Item Type: {item.itemType.name}");

    else:
        print("Lista przedmiotów jest pusta.")

def ShowStats():
    print(f"statystyki {chatacterName}: ")
    time.sleep(1.0)
    weapon = Data.itemsList[weaponID];
    arrmor = Data.itemsList[arrmorID];
    totalMaxHp = maxHitPoints + weapon.hitPoints + arrmor.hitPoints;
    totalAtk = attak + weapon.attak + arrmor.attak;
    totalDef = defence + weapon.defence + arrmor.defence;
    print(f"Zdrowie: {totalMaxHp}/{hitPoints}");
    time.sleep(0.1)
    print(f"Atak: {totalAtk}");
    time.sleep(0.1)
    print(f"Obrona: {totalDef}");
    time.sleep(0.1)
    print(f"poziom: {level} ")
    time.sleep(0.1)
    print(f"exp: {exp} ")

def ShowEquipment():
    print("Twoje wyposarzenie i ich statystyki");
    time.sleep(0.5)
    if weaponID ==0:
        print("nie posiadasz żadnej broni");
    else:
        item = Data.itemsList [weaponID];
        print("Broń w posiadaniu");
        print(f"Name: {item.name}");
        print(f"Value: {item.value}");
        print(f"Attack: {item.attak}");
        print(f"Defence: {item.defence}");
        print(f"Hit Points: {item.hitPoints}\n");
    time.sleep(0.5)
    if arrmorID ==0:
        print("Nie posiadasz żadnej zbroi");
        
    else:
        item = Data.itemsList [arrmorID];
        print("Zbroja w posiadaniu");
        print(f"Name: {item.name}");
        print(f"Value: {item.value}");
        print(f"Attack: {item.attak}");
        print(f"Defence: {item.defence}");
        print(f"Hit Points: {item.hitPoints}\n");

def ChangeArmor():
    global arrmorID;
    print("Twoja zbroja:")
    time.sleep(0.5)
    if arrmorID == 0:
        print("Nie posiadasz żadnej zbroi.")
    else:
        item = Data.itemsList[arrmorID]
        print("Zbroja w posiadaniu:")
        print(f"Name: {item.name}")
        print(f"Value: {item.value}")
        print(f"Defence: {item.defence}")
        print(f"Hit Points: {item.hitPoints}\n")

    print("Dostępne zbroje w twoim ekwipunku:")
    availableArmors = {}
    if itemsId:
        for thisItemId in itemsId:
            item = Data.itemsList[thisItemId]
            time.sleep(0.1)
            if item.itemType == Classes.ItemType.ARMOR:
                print(f"{thisItemId} - Name: {item.name} | Hit Points: {item.hitPoints} | Defence: {item.defence}")
                availableArmors[thisItemId] = item

        if availableArmors:
            newArmorID = input("Wpisz ID zbroi, na którą chcesz zmienić: ")
            if newArmorID.isdigit() and int(newArmorID) in availableArmors:
                arrmorID = int(newArmorID)
                print(f"Zmieniono zbroję na: {availableArmors[arrmorID].name}")
            else:
                print("Niepoprawne ID zbroi.")
        else:
            print("Nie posiadasz żadnej innej zbroi.")
    else:
        print("Nie posiadasz żadnej zbroi.")
    
def ChangeWeapon():
    global weaponID;
    print("Twoja broń:")
    time.sleep(0.5)
    if weaponID == 0:
        print("Nie posiadasz żadnej broni.")
    else:
        item = Data.itemsList[weaponID]
        print("Broń w posiadaniu:")
        print(f"Name: {item.name}")
        print(f"Value: {item.value}")
        print(f"Attack: {item.attak}")
        print(f"Defence: {item.defence}")
        print(f"Hit Points: {item.hitPoints}\n")

    print("Dostępne bronie w twoim ekwipunku:")
    availableWeapons = {}
    if itemsId:
        for thisItemId in itemsId:
            time.sleep(0.1)
            item = Data.itemsList[thisItemId]
            if item.itemType == Classes.ItemType.WEAPON:
                print(f"{thisItemId} - Name: {item.name} | Hit Points: {item.hitPoints} | Attack: {item.attak} | Defence: {item.defence}")
                availableWeapons[thisItemId] = item

        if availableWeapons:
            newWeaponID = input("Wpisz ID broni, na którą chcesz zmienić: ")
            if newWeaponID.isdigit() and int(newWeaponID) in availableWeapons:
                weaponID = int(newWeaponID)
                print(f"Zmieniono broń na: {availableWeapons[weaponID].name}")
            else:
                print("Niepoprawne ID broni.")
        else:
            print("Nie posiadasz żadnej innej broni.")
    else:
        print("Nie posiadasz żadnej broni.")


#aftermach
def PlayerDead():
    sys.exit()

def PlayerVictory():
    DidPlayerLevelUp()

def DidPlayerLevelUp():
    global exp,level,maxHitPoints,attak,defence

    expFornextLevel = level*15
    if exp >= expFornextLevel:
        level +=1;
        exp = exp -expFornextLevel;

        maxHitPoints+2
        if level %3==0:
            attak +1
        if level %5 ==0:
            defence +1
        print(f"Awansowałes na poziom {level} statystyki zostały zwiekszone") 
    time.sleep(1.1)
    
#system
def ImportData():
    Data.ImportEnemy();
    Data.ImportItems();
    Data.ImportLocation();
    Data.ImportEvent();
    Data.ImportRedward();
    Data.ImportShop();
    Data.ImportTrap();

def DebugFiles():
    Debug.print_enemy_list(Data.enemyList);
    Debug.print_items_list(Data.itemsList);
    Debug.print_location_list(Data.locationList);
    Debug.print_events_list(Data.eventsList);
    Debug.print_shops_list(Data.shopList);
    Debug.print_traps_list(Data.trapsList);
    Debug.print_rewards_list(Data.rewardList);
