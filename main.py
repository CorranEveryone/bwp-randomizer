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
#   Bedwars Eight Team (!)
#   Bedwars Four Team (!)
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
    itemnames = ["Wool Count", "Knockback Stick", "Bow", "Arrows", "Use shears", "Ender Pearls", "Sword Tier", "Sword Sharpness", "Armour Tier", "Ladders", "Fireballs", "TNT", "Random Item Bonus", "Bridge Eggs", "Iron Golems", "Fishing Rods", "Snow Balls / Silverfish", "Juke Box", "Pop up towers", "Fireball Bow", "Rapid Fire", "Aimbot", "Emerald Gen Speed", "Diamond Gen Speed", "Starting Diamonds", "Forge Speed", "Golden Apple on Kill", "Summon ender dragon on Start", "Ender Dragon Block Destruction", "Combo PVP (no hit delay)", "Respawn Length", "Instant Block Break", "Allow Map to be Broken", "Allow Placements Anywhere", "Double Jump", "Double Jump Power", "Kill Effects", "Rising Lava", "Falling anvils", "Random Enderpearls", "Random MLG Clutch", "MLG Clutch Mode", "Random TNT Spawns", "Chicken Head", "OP Shop Items", "Mob Shop Items", "Wool Allergy (Not Recommended for this)", "OP Generators", "Random Potion Effect", "Timed Effects", "Random Health", "Random Health Range", "Desync Health", "Life Steal [Can lead to softlocks]", "Bed Defence", "Click Reducer", "Allow Crafting", "Random Block Placing", "Random Item Drops", "Random Item On Kill", "XP Level", "Allow Armour Swapping", "Create bedrock walls [SET TO 1 MINUTE OR DISABLED, YOU DO NOT WANT TO WAIT 20 MINUTES, TRUST]", "Explosion Power", "Jump Boost Effect", "Speed Effect", "Blindness Effect", "Health", "Fall Damage", "Spawn protection time", "Allow Chat", "Start game tweak message", "Kill Messages", "Allow Projectiles", "Increased Diamond Costs", "Convert Eight-team Maps"]
    itemdefs = []
elif gamemode == "Bedwars 8 Teams":
    fullpages = 2
    lastpage_fullrows = 0
    lastrow_items = 4
    itemnames = ["Wool Count", "Knockback Stick", "Bow", "Arrows", "Use shears", "Ender Pearls", "Sword Tier", "Sword Sharpness", "Armour Tier", "Ladders", "Fireballs", "TNT", "Random Item Bonus", "Bridge Eggs", "Iron Golems", "Fishing Rods", "Snow Balls / Silverfish", "Juke Box", "Pop up towers", "Fireball Bow", "Rapid Fire", "Aimbot", "Emerald Gen Speed", "Diamond Gen Speed", "Starting Diamonds", "Forge Speed", "Golden Apple on Kill", "Summon ender dragon on Start", "Ender Dragon Block Destruction", "Combo PVP (no hit delay)", "Respawn Length", "Instant Block Break", "Allow Map to be Broken", "Allow Placements Anywhere", "Double Jump", "Double Jump Power", "Kill Effects", "Rising Lava", "Falling anvils", "Random Enderpearls", "Random MLG Clutch", "MLG Clutch Mode", "Random TNT Spawns", "Chicken Head", "OP Shop Items", "Mob Shop Items", "Wool Allergy (Not recommended for this)", "OP Generators", "Random Potion Effect", "Timed Effects", "Random Health", "Random Health Range", "Desync Health", "Life Steal [Can lead to softlocks]", "Bed Defence", "Elemental Bedwars", "Click Reducer", "Allow Crafting", "Random Block Placing", "Random Item Drops", "Random Item On Kill", "XP Level", "Allow Armour Swapping", "Create bedrock walls [SET TO 1 MINUTE OR DISABLED, YOU DO NOT WANT TO WAIT 20 MINUTES, TRUST]", "Explosion Power", "Jump Boost Effect", "Speed Effect", "Blindness Effect", "Health", "Fall Damage", "Spawn protection time", "Allow Chat", "Start game tweak message", "Kill Messages", "Allow Projectiles", "Increased Diamond Costs"]
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
        {"name":"Random Item Bonus", "rank":"Master", "note":"It's random item on kill, not like the Random Ender Pearls."},
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
        {"name":"Double Jump Power", "rank":"Master"}
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
    try:
        print(itemnames[randomvalue-1])
        print("Item is not using an Item Definition, it is possible to be locked behind a rank.")
    except IndexError:
        print("ERROR, ITEM NAME AND DEFINITION NOT FOUND")