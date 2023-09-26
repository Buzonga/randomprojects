# Código escrito pelo Buzo, me da crédito se for usar XD

import random

## inputs 
### Input to see if the weapon have an attack value that must be rolled.

squad_size = int(input("How many models does your unity have?"))
if str(input("Does the weapon's attack characteristic have a dice to be rolled? (Yes/No)")) == "Yes":
    attack_dice_prefix = int(input("How many dices have to be rolled?"))
    d_sulfix = int(input("How many faces does the dice have?"))
    attack_dices_rolled = []
    for total_squad_attacks in range(squad_size):    
        for atk_die_roll in range(attack_dice_prefix):
         attack_number_roll = random.randint(1, d_sulfix)
         attack_dices_rolled.append(int(attack_number_roll))
         print(f"Attack number roll {attack_number_roll, sum(attack_dices_rolled)}")
    if str(input("Does the number of attack dices have any more attacks? (Yes/No)")) == "Yes":
        more_attacks = int(input("How many?"))
        weapon_attacks = sum(attack_dices_rolled + [(more_attacks * squad_size)])
    else:
        weapon_attacks = sum(attack_dices_rolled)
else:
    weapon_attacks = int(input("How many attacks does the weapon have?")) * squad_size

print(f"{weapon_attacks} weapon attacks")

### Balistics or Weapon skill
skill = int(input("What is the skill of the squad?"))

### Number of attacks of the weapon
num_dice = weapon_attacks

### Strengh of the weapon
weapon_strengh = int(input("What is the strengh of the weapon?"))

###AP of the weapon
weapon_armour_penetration = int(input("What is the AP of the weapon?"))

### Dammage of the weapon
weapon_dammage = (input("What is the weapon dammage?"))

###toughness of the enemy unity
enemy_toughness = int(input("What is the toughness of the enemy unity?"))

###Saving throw of the enemy unity
enemy_save = int(input("What is the enemy saving throw?"))

## Hit Rolls
misses = []
hits = []
critical_hits = []

for hit_die in range(num_dice):
    hit_dice_roll = random.randint(1, 6)
    if hit_dice_roll == 6:
        critical_hits.append(hit_dice_roll)
    elif hit_dice_roll >= skill:
        hits.append(hit_dice_roll)
    else:
        misses.append(hit_dice_roll)
    
print(f"You have rolled {misses} as hit misses, {hits} as hit hits, {critical_hits} as hit critical_hits")
result_hits = f"You have rolled {len(misses)} misses {len(hits)} hits and {len(critical_hits)} critical hits!"
print(result_hits)

## Wound Rolls

if weapon_strengh >= 2 * enemy_toughness:
    wound_difficulty = 2
elif weapon_strengh > enemy_toughness:
    wound_difficulty = 3
elif weapon_strengh == enemy_toughness:
    wound_difficulty = 4
elif weapon_strengh < enemy_toughness / 2:
    wound_difficulty = 6
elif weapon_strengh < enemy_toughness:
    wound_difficulty = 5

wound_misses = []
wound_hits = []
wound_critical = []

for wound_die in range(len(hits + critical_hits)):
    wound_dice_roll = random.randint(1, 6)
    if wound_dice_roll == 6:
        wound_critical.append(wound_dice_roll)
    elif wound_dice_roll >= wound_difficulty:
        wound_hits.append(wound_dice_roll)
    else:
        wound_misses.append(wound_dice_roll)

print(f"You have rolled{wound_misses} as wound misses, {wound_hits} as wound hits, {wound_critical} as wound critical hits")
result_wounds = f"You have rolled {len(wound_misses)} wounds misses, {len(wound_hits)} wounds and {len(wound_critical)} critical wounds!"
print(result_wounds)

## Saving Throws

saved_saves = []
failed_saves = []

### cover test
if input("Does the enemy unit have cover? (Yes/No)") == "Yes":
    if weapon_armour_penetration == 0 and enemy_save <= 3:
        cover = 0
else:
    cover = 1

for save_die in range(len(wound_hits + wound_critical)):
    save_dice_roll = random.randint(1, 6)
    if save_dice_roll - weapon_armour_penetration + cover >= enemy_save:
        saved_saves.append(save_dice_roll)
    else:
        failed_saves.append(save_dice_roll)

print(f"They rolled{saved_saves} as saved, {failed_saves} as misses")
result_saves = f"He saved {len(saved_saves)} and failed {len(failed_saves)}!"
print(result_saves)

## rolling dices if the weapon have to roll for dammage

if failed_saves != 0:
    if "d" in weapon_dammage:
        dammage_dice_prefix = int(input("How many dices have to be rolled?"))
        dammage_dice_sulfix = int(input("How many faces does the dice have?"))
        dammage_dices_rolled = []
        for roll_dam_die in range(len(failed_saves)):
            for damdie_roll in range(dammage_dice_prefix):
                dammage_dice_rolls = random.randint(1, dammage_dice_sulfix)
                dammage_dices_rolled.append(dammage_dice_rolls)
        if input("Does the dammage have to add something?(Yes/No)") == "Yes":
            extra_dammage_in_dammage_dice = int(input("How much?"))
            final_dammage = []
            for i in range(len(dammage_dices_rolled)):
                dammage_dices_rolled[i] += extra_dammage_in_dammage_dice
    else:
        dammage_dices_rolled = weapon_dammage
else:
    print("You didn't cause any dammage.")

print(f"Your dammage for each wound was: {dammage_dices_rolled}")

## Resulting dammage

result_dammage = f"You dealed {len(failed_saves)} wounds, each one having {weapon_dammage} dammage."

## Results
print(result_hits)
print(result_wounds)
print(result_saves)
print(result_dammage)