#______  _    _______  ______                _                 _              
#| ___ \| |  | | ___ \ | ___ \              | |               (_)             
#| |_/ /| |  | | |_/ / | |_/ /__ _ _ __   __| | ___  _ __ ___  _ _______ _ __ 
#| ___ \| |/\| |  __/  |    // _` | '_ \ / _` |/ _ \| '_ ` _ \| |_  / _ \ '__|
#| |_/ /\  /\  / |     | |\ \ (_| | | | | (_| | (_) | | | | | | |/ /  __/ |   
#\____/  \/  \/\_|     \_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|_/___\___|_|   
#
# Legend:
#   (x) = Not Implemented
#   (!) = Outdated Implementations
#
# Gamemodes:
#   Bed Bridge Fight (x)
#   Four Way Bridge Fight (x)
#   Competitive Bridge (x)
#   Obstacle (x)
#   Sumo (x)
#   Sumo Duels (x)
#   Ground Duel (x)
#   Resource Collect (x)
#   Old Resource Collect (x)
#   Void Fight (x)
#   Stick Fight (x)
#   Party Games (x)
#   Beta Sumo (x)
#   Bow Fight (x)
#   Pearl Fight (x)
#   Bed Rush (x)
#   Ladder Fight (x)
#   Flat Fight (x)
#   Bedwars Normal (x)
#   Bedwars Late Game (x)
#   Bedwars Mega (x)
#   Bedwalls (x)
#   Ranked Fours Practice (x)
#   Bedwars Eight Team
#   Bedwars Four Team
#   Miniwars (x)
#   Bedwars Rush Duels (x)
#   Sky Conquer (x)
#   Autobox (x)
#

import random

# CONFIG
gamemode = "Bedwars 8 Teams" # Pick a gamemode from above
playerrank = "Master" # Your rank should either be "Member", "Adept", "Expert", and "Master" (Anyone above just use Master)

# CODE
rowsperpage = 4
itemsperrow = 9

if gamemode == "Bedwars 4 Teams":
    fullpages = 2
    lastpage_fullrows = 0
    lastrow_items = 4
    itemdefs = [
        {"name":"Wool Count"},
        {"name":"Knockback Stick", "rank":"Adept"},
        {"name":"Bow"},
        {"name":"Arrows"},
        {"name":"Use shears"},
        {"name":"Ender Pearls", "rank":"Expert"},
        {"name":"Sword Tier"},
        {"name":"Sword Sharpness"},
        {"name":"Armour Tier"},
        {"name":"Ladders", "rank":"Adept"},
        {"name":"Fireballs", "rank":"Adept"},
        {"name":"TNT", "rank":"Adept"},
        {"name":"Random Item Bonus", "rank":"Master", "note":"I actually have no clue what this does, if you can tell me, that would be great."},
        {"name":"Bridge Eggs", "rank":"Expert"},
        {"name":"Iron Golems", "rank":"Expert"},
        {"name":"Fishing Rods", "rank":"Adept"},
        {"name":"Snow Balls / Silverfish", "rank":"Adept"},
        {"name":"Juke Box", "rank":"Master"},
        {"name":"Pop up towers", "rank":"Expert"},
        {"name":"Fireball Bow", "rank":"Master"},
        {"name":"Rapid Fire", "rank":"Master"},
        {"name":"Aimbot", "rank":"Master"},
        {"name":"Emerald Gen Speed", "rank":"Adept"},
        {"name":"Diamond Gen Speed", "rank":"Adept"},
        {"name":"Starting Diamonds", "rank":"Adept"},
        {"name":"Forge Speed", "rank":"Adept"},
        {"name":"Golden Apple on Kill", "rank":"Expert"},
        {"name":"Summon ender dragon on Start", "rank":"Master"},
        {"name":"Ender Dragon Block Destruction"},
        {"name":"Combo PVP (no hit delay)", "rank":"Master", "note":"Don't stand in fire"},
        {"name":"Respawn Length"},
        {"name":"Instant Block Break", "rank":"Adept"},
        {"name":"Allow Map to be Broken", "rank":"Master"},
        {"name":"Allow Placements Anywhere", "rank":"Master"},
        {"name":"Double Jump", "rank":"Expert"},
        {"name":"Double Jump Power", "rank":"Master"},
        {"name":"Kill Effects", "rank":"Expert"},
        {"name":"Rising Lava", "rank":"Master"},
        {"name":"Falling anvils", "rank":"Master"},
        {"name":"Random Enderpearls", "rank":"Master"},
        {"name":"Random MLG Clutch", "rank":"Master"},
        {"name":"MLG Clutch Mode", "rank":"Master"},
        {"name":"Random TNT Spawns", "rank":"Master"},
        {"name":"Chicken Head", "rank":"Master"},
        {"name":"OP Shop Items", "rank":"Master"},
        {"name":"Mob Shop Items", "rank":"Expert"},
        {"name":"Wool Allergy", "rank":"Master"},
        {"name":"OP Generators", "rank":"Master"},
        {"name":"Random Potion Effects", "rank":"Master"},
        {"name":"Timed Effects", "rank":"Master"},
        {"name":"Random Health", "rank":"Master"},
        {"name":"Random Health Range", "rank":"Master"},
        {"name":"Desync Health", "rank":"Master"},
        {"name":"Life Steal", "rank":"Expert", "note":"Due to bugs, this option can cause softlocks when a player runs out of hearts before their bed is destroyed. They will count as alive even though they have been long since been Final killed. ENABLE AT YOUR OWN RISK."},
        {"name":"Bed Defence", "rank":"Adept"},
        {"name":"Click Reducer"},
        {"name":"Allow Crafting", "rank":"Master"},
        {"name":"Random Block Placing", "rank":"Adept", "note":"Good luck placing blocks"},
        {"name":"Random Item Drops", "rank":"Adept"},
        {"name":"Random Item On Kill", "rank":"Adept"},
        {"name":"XP Level"},
        {"name":"Allow Armour Swapping"},
        {"name":"Create bedrock walls", "rank":"Master", "note":"Set it to 1 minute or disable if already set to 1 minute. DO NOT SET IT TO 20 MINUTES, YOU WILL NOT BE ABLE TO DO ANYTHING."},
        {"name":"Explosion Power", "rank":"Expert"},
        {"name":"Jump Boost Effect", "rank":"Adept"},
        {"name":"Speed Effect", "rank":"Adept"},
        {"name":"Blindness Effect", "rank":"Expert"},
        {"name":"Health", "rank":"Expert"},
        {"name":"Fall Damage"},
        {"name":"Spawn protection time"},
        {"name":"Allow Chat"},
        {"name":"Start game tweak message"},
        {"name":"Kill Messages"},
        {"name":"Allow Projectiles", "rank":"Adept"},
        {"name":"Increased Diamond Costs", "rank":"Adept"},
        {"name":"Convert Eight-team Maps", "rank":"Master"}
    ]
elif gamemode == "Bedwars 8 Teams":
    fullpages = 2
    lastpage_fullrows = 0
    lastrow_items = 4
    itemdefs = [
        {"name":"Wool Count"},
        {"name":"Knockback Stick", "rank":"Adept"},
        {"name":"Bow"},
        {"name":"Arrows"},
        {"name":"Use shears"},
        {"name":"Ender Pearls", "rank":"Expert"},
        {"name":"Sword Tier"},
        {"name":"Sword Sharpness"},
        {"name":"Armour Tier"},
        {"name":"Ladders", "rank":"Adept"},
        {"name":"Fireballs", "rank":"Adept"},
        {"name":"TNT", "rank":"Adept"},
        {"name":"Random Item Bonus", "rank":"Master", "note":"I actually have no clue what this does, if you can tell me, that would be great."},
        {"name":"Bridge Eggs", "rank":"Expert"},
        {"name":"Iron Golems", "rank":"Expert"},
        {"name":"Fishing Rods", "rank":"Adept"},
        {"name":"Snow Balls / Silverfish", "rank":"Adept"},
        {"name":"Juke Box", "rank":"Master"},
        {"name":"Pop up towers", "rank":"Expert"},
        {"name":"Fireball Bow", "rank":"Master"},
        {"name":"Rapid Fire", "rank":"Master"},
        {"name":"Aimbot", "rank":"Master"},
        {"name":"Emerald Gen Speed", "rank":"Adept"},
        {"name":"Diamond Gen Speed", "rank":"Adept"},
        {"name":"Starting Diamonds", "rank":"Adept"},
        {"name":"Forge Speed", "rank":"Adept"},
        {"name":"Golden Apple on Kill", "rank":"Expert"},
        {"name":"Summon ender dragon on Start", "rank":"Master"},
        {"name":"Ender Dragon Block Destruction"},
        {"name":"Combo PVP (no hit delay)", "rank":"Master", "note":"Don't stand in fire"},
        {"name":"Respawn Length"},
        {"name":"Instant Block Break", "rank":"Adept"},
        {"name":"Allow Map to be Broken", "rank":"Master"},
        {"name":"Allow Placements Anywhere", "rank":"Master"},
        {"name":"Double Jump", "rank":"Expert"},
        {"name":"Double Jump Power", "rank":"Master"},
        {"name":"Kill Effects", "rank":"Expert"},
        {"name":"Rising Lava", "rank":"Master"},
        {"name":"Falling anvils", "rank":"Master"},
        {"name":"Random Enderpearls", "rank":"Master"},
        {"name":"Random MLG Clutch", "rank":"Master"},
        {"name":"MLG Clutch Mode", "rank":"Master"},
        {"name":"Random TNT Spawns", "rank":"Master"},
        {"name":"Chicken Head", "rank":"Master"},
        {"name":"OP Shop Items", "rank":"Master"},
        {"name":"Mob Shop Items", "rank":"Expert"},
        {"name":"Wool Allergy", "rank":"Master"},
        {"name":"OP Generators", "rank":"Master"},
        {"name":"Random Potion Effects", "rank":"Master"},
        {"name":"Timed Effects", "rank":"Master"},
        {"name":"Random Health", "rank":"Master"},
        {"name":"Random Health Range", "rank":"Master"},
        {"name":"Desync Health", "rank":"Master"},
        {"name":"Life Steal", "rank":"Expert", "note":"Due to bugs, this option can cause softlocks when a player runs out of hearts before their bed is destroyed. They will count as alive even though they have been long since been Final killed. ENABLE AT YOUR OWN RISK."},
        {"name":"Bed Defence", "rank":"Adept"},
        {"name":"Elemental Bedwars", "rank":"Master"},
        {"name":"Click Reducer"},
        {"name":"Allow Crafting", "rank":"Master"},
        {"name":"Random Block Placing", "rank":"Adept", "note":"Good luck placing blocks"},
        {"name":"Random Item Drops", "rank":"Adept"},
        {"name":"Random Item On Kill", "rank":"Adept"},
        {"name":"XP Level"},
        {"name":"Allow Armour Swapping"},
        {"name":"Create bedrock walls", "rank":"Master", "note":"Set it to 1 minute or disable if already set to 1 minute. DO NOT SET IT TO 20 MINUTES, YOU WILL NOT BE ABLE TO DO ANYTHING."},
        {"name":"Explosion Power", "rank":"Expert"},
        {"name":"Jump Boost Effect", "rank":"Adept"},
        {"name":"Speed Effect", "rank":"Adept"},
        {"name":"Blindness Effect", "rank":"Expert"},
        {"name":"Health", "rank":"Expert"},
        {"name":"Fall Damage"},
        {"name":"Spawn protection time"},
        {"name":"Allow Chat"},
        {"name":"Start game tweak message"},
        {"name":"Kill Messages"},
        {"name":"Allow Projectiles", "rank":"Adept"},
        {"name":"Increased Diamond Costs", "rank":"Adept"}
    ]
else: # Loaded Nothing
    print(f"'{gamemode}' is not a valid gamemode")
    exit()

totalitems = (fullpages*rowsperpage*itemsperrow)+(lastpage_fullrows*itemsperrow)+(lastrow_items)

while True:
    randomvalue = random.randint(1, totalitems)
    try:
        if itemdefs[randomvalue-1]["rank"] == "Member":
            break 
        elif itemdefs[randomvalue-1]["rank"] == "Adept" and (playerrank == "Adept" or playerrank == "Expert" or playerrank == "Master"):
            break
        elif itemdefs[randomvalue-1]["rank"] == "Expert" and (playerrank == "Expert" or playerrank == "Master"):
            break
        elif itemdefs[randomvalue-1]["rank"] == "Master" and playerrank == "Master":
            break
        else:
            try:
                print(f"Rolled {randomvalue} ({itemdefs[randomvalue-1]["name"]}) but player doesn't have a sufficient rank.")
            except IndexError:
                print(f"Rolled {randomvalue} but player doesn't have a sufficient rank.")
    except IndexError:
        break
    except KeyError:
        break
randomitem = randomvalue
randomrow = 1
randompage = 1


while randomitem > itemsperrow:
    randomitem -= itemsperrow
    randomrow += 1
while randomrow > rowsperpage:
    randomrow -= rowsperpage
    randompage += 1

print(f"#{randomvalue}")
print()
print(f"Page: {randompage}")
print(f"Row: {randomrow}")
print(f"Item: {randomitem}")
print()
try:
    print(itemdefs[randomvalue-1]["name"])
    try:
        print(f"NOTE: {itemdefs[randomvalue-1]["note"]}")
    except KeyError:
        pass
except IndexError:
    print(f"ERROR: ITEM DEFINITION NOT FOUND ({randomvalue})")
    print(f"Gamemode: {gamemode}")
    print(f"Player Rank: {playerrank}")
    print("Item Definition Dump:")
    print(itemdefs)