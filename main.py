from enemy import Enemy
from player import Player

player = Player()
enemy_list = [Enemy(type = "Zombie"), Enemy(type = "Skeleton")]

while True:
    try:
        # checks if all enemies are alive or not
        enemies_alive = True
        living_counter = 0
        for enemy in enemy_list:
            if enemy.get_health() > 0:
                living_counter += 1
        if living_counter == 0:
            enemies_alive = False

        if enemies_alive:
            # Print out user info
            print(player)
            # Print out the enemy list
            selection_number = 1
            for enemy in enemy_list:
                print(f"[{selection_number}] {enemy}")
                selection_number += 1
            print()

            # PLAYER TURN
            attack_or_heal_choice = input("[A] Attack Enemy | [B] Heal: ").upper()
            if attack_or_heal_choice == "B":
                player.heal()
                print("The player has healed for 50 points!")
                print(f"The player now has {player.get_current_health} / {player.get_max_health()}.")
            elif attack_or_heal_choice == "A":
                choice = int(input("Which enemy would you like to attack? "))
                selected_enemy = enemy_list[choice - 1]

                if selected_enemy.get_health() > 0:
                    player.attack(selected_enemy)
                else:
                    print("This enemy is dead!")
            else:
                raise ValueError
            
            print()
            # ENEMY TURN
            for enemy in enemy_list:
                if enemy.get_health() > 0:
                    enemy.attack(player)
                    print(enemy - 1)

        else:
            print("All enemies are dead. You Win!")
            break
    except ValueError:
        print("Please enter A or B to either attack the enemy or heal yourself.")
    except Exception as e:
        print(f"An error occured: {e}")

