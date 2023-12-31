import Data
import Game
import Classes
import time

global playerBattleMaxHp,playerBattleDef,playerBattleAtak;
global Enemy;
global enemyHp,enemyAttak,enemyDef;

def BattleSetUpStats(EnemyID):
    global playerBattleMaxHp,playerBattleDef,playerBattleAtak;
       
    weapon = Data.itemsList[Game.weaponID];
    arrmor = Data.itemsList[Game.arrmorID];

    playerBattleMaxHp = Game.maxHitPoints + weapon.hitPoints + arrmor.hitPoints;
    playerBattleAtak = Game.attak + weapon.attak + arrmor.attak;
    playerBattleDef = Game.defence + weapon.defence + arrmor.defence;
    #dodawanie wroga
    global Enemy, enemyHp, enemyAttak, enemyDef;
    Enemy =  Data.enemyList[EnemyID];
    
    HpMultiplayer = 1.00
    if Game.difficulty == Classes.Difficulty.EASY:
        HpMultiplayer = 0.75
    elif Game.difficulty == Classes.Difficulty.MEDIUM:
        HpMultiplayer = 1.00
    elif Game.difficulty == Classes.Difficulty.HARD:
        HpMultiplayer = 1.50

    enemyHp = Enemy.hitPoints * HpMultiplayer;
    enemyAttak = Enemy.attack;
    enemyDef = Enemy.defence;

def BattleStart(EnemyID):
    BattleSetUpStats(EnemyID)
    PlayerTurn()

def PlayerTurn():
    print(f"{Game.chatacterName} atakuje {Enemy.name} zadajać {EnemyTakedamage(playerBattleAtak)}")
    if enemyHp <= 0:
        print(f"udalo ci się pokonać {Enemy.name}")
        print(f"zyskujesz {Enemy.expDrop} doświatczenia i {Data.level} złota")
        Game.exp += Enemy.expDrop
        Game.gold += Game.level
        Game.PlayerVictory();
    else:
      time.sleep(0.7)
      EnemyTurn(); 

def EnemyTurn():
    print(f"{Enemy.name} zadaje ci {PlayerTakeDamage(enemyAttak)} obrażeń")
    if Game.hitPoints <=0:
        print(f"po cieżkiej walce {Game.chatacterName} odchodzi w zaswiaty")
        Game.PlayerDead();
    else:
        print(f"posiadasz {playerBattleMaxHp}/{Game.hitPoints}")
        time.sleep(0.7)
        PlayerTurn();

def PlayerTakeDamage(Damage):
    if playerBattleDef >= Damage:
        Damage = 1
    else:
        Damage = Damage-playerBattleDef

    Game.hitPoints -= Damage
    return Damage

def EnemyTakedamage(Damage):
    global enemyHp
    if enemyDef >= Damage:
        Damage = 1
    else:
        Damage -= enemyDef
        enemyHp -= Damage;
    return Damage
    