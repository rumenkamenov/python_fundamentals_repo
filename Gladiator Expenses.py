lost_figth_count = int(input())

helmet_price = float(input())
sword_proce = float(input())
shield_price = float(input())
armour_price = float(input())

helmet_count = 0
sword_count = 0

for game in range(1, lost_figth_count + 1):
    if game % 2 == 0:
        helmet_count += 1
    elif game % 3 == 1:
        sword_count += 1
    
shield_count = lost_figth_count - (sword_count*helmet_count)

sum_helmet = helmet_count * helmet_price
sum_sword = sword_count * sword_proce
sum_shield = shield_count * shield_price
total = sum_helmet + sum_sword + sum_shield

#print(f"Trashed helmet -> {helmet_count} times")
#print(f"Trashed sword -> {sword_count} times")
#print(f"Trashed shield -> {shield_count} times")
print(f"Gladiator expenses: {total:.2f} aureus")
