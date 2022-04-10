import random


def print_stats():
    print("Player: " + str(player_hp) + "HP " + str(player_atk) + "ATK")
    print("Enemy: " + str(enemy_hp) + "HP " + str(enemy_atk) + "ATK")

enemies = ["golem", "goblin", "zsuzsi"]
enemy_name = enemies[random.randrange(0, len(enemies))]

player_hp = 100
enemy_hp = 100
player_atk = 10
enemy_atk = 12


while player_hp > 0 and enemy_hp > 0:
    print_stats()

    if player_hp > 0:
        print()

        print("megütötted a(z) " + enemy_name)

        bonus = random.randrange(-3, 3 + 1)
        enemy_hp = enemy_hp - (player_atk + bonus)
        if bonus == 3:
            print("super effective volt")
        elif bonus == -3:
            print("szar volt")

    if enemy_hp > 0:
        print()

        print("a(z) " + enemy_name + " megütött téged")
        bonus = random.randrange(-3, 3 + 1)
        player_hp = player_hp - (enemy_atk + bonus)
        if bonus == 3:
            print("super effective volt")
        if bonus == -3:
            print("szar volt")

    print()

    print_stats()

    if player_hp > 0 and enemy_hp > 0:
        input()

if player_hp > 0:
    print("Gyöztél")
else:
    print("Game Over")
