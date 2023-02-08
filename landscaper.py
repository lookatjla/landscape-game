############################
######## Game State ########
############################

game = {"equipment_type": 0, "money": 0} # this is what we start out with in our game

all_equipment = [
    {"type": "teeth", "profit": 1, "cost": 0},
    {"type": "rusty scissors", "profit": 5, "cost": 5},
    {"type": "average push lawnmower", "profit": 50, "cost": 25},
    {"type": "fancy battery-powered lawnmower", "profit": 100, "cost": 250},
    {"type": "broke college kids", "profit": 250, "cost": 500}
]



############################
### Game Option Function ###
############################

def cut_lawn():
    equipment_type = all_equipment[game["equipment_type"]]
    print(f"You cut a lawn with your {equipment_type['type']} and make {equipment_type['profit']}.")
    game["money"] += equipment_type["profit"]
    
    
def game_stats():
    equipment_type = all_equipment[game["equipment_type"]]
    print(f"You currently have {game['money']} and are using your {equipment_type['type']}.")
    
    
def upgrade():
    if (game["equipment_type"] >= len(all_equipment) -1):
        print("There are no more upgrades available.")
        return 0
    equipment_upgrade = all_equipment[game["equipment_type"]+1]
    if (equipment_upgrade == None):
        print("There is no more equipment.")
        return 0
    if (game["money"] < equipment_upgrade["cost"]):
        print("You do not have enough money to make upgrades.")
        return 0
    print("You have upgraded your equipment.")
    game["money"] -= equipment_upgrade["cost"]
    game["equipment_type"] += 1
    

def win_check():
    if (game["equipment_type"] == 1 and game["money"] >= 1000):
        print("You win!")
        return True
    return False
    
while (True):
    i = input("[1] Cut Lawns [2] Game Stats [3] Upgrade [4] Quit")
    
    i = int(i)
    
    if (i == 1):
        cut_lawn()
    if (i == 2):
        game_stats()
    if (i ==3):
        upgrade()
    if (i ==4):
        print("You quit the game.")
        break
    if (win_check()):
        break