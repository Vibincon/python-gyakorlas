import random

enemies = ["golem", "goblin", "zsuzsi"]
enemy_name = enemies[random.randrange(0, len(enemies))]

player_hp = 100
enemy_hp = 100
player_atk = 10
enemy_atk = 12

print("Player: " + str(player_hp) + "HP " + str(player_atk) + "ATK")
print("Enemy: " + str(enemy_hp) + "HP " + str(enemy_atk) + "ATK")

print()

print("megütötted a(z) " + enemy_name)

bonus = random.randrange(-3, 3 + 1)
enemy_hp = enemy_hp - (player_atk + bonus)
if bonus == 3:
    print("super effective volt")
elif bonus == -3:
    print("szar volt")

print()

print("a(z) " + enemy_name + " megütött téged")
bonus = random.randrange(-3, 3 + 1)
player_hp = player_hp - (enemy_atk + bonus)
if bonus == 3:
    print("super effective volt")
if bonus == -3:
    print("szar volt")

print()

print("Player: " + str(player_hp) + "HP " + str(player_atk) + "ATK")
print("Enemy: " + str(enemy_hp) + "HP " + str(enemy_atk) + "ATK")
