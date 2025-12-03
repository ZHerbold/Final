from enemy import Enemy
from player import Player
from floor import Floor

player = Player()
tower = []
for i in range(10):
    tower.append(Floor(i+1))

tower_mob_list = []
for floor in tower:
    floor.spawn_mobs()
    tower_mob_list.append(floor.get_mob_list())
current_floor = 0
while True:
    try:
        enemy_list = tower_mob_list[current_floor]
        # checks if all enemies are alive or not
        enemies_alive = True
        player_alive = True
        living_counter = 0
        for enemy in enemy_list:
            if enemy.get_health() > 0:
                living_counter += 1
        if living_counter == 0:
            enemies_alive = False

        if enemies_alive and player_alive:
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
                print(f"The player now has {player.get_current_health()} / {player.get_max_health()}.")
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
        elif player_alive == False:
            print("YOU DIED!")
            break
        else:
            print("All enemies are dead. You Win!")
            player.gain_experience(tower[current_floor].give_xp())
            current_floor = current_floor + 1
            print("MOVING TO THE NEXT FLOOR!\nFLOOR", current_floor + 1)
    except ValueError:
        print("Please enter A or B to either attack the enemy or heal yourself.")
    except Exception as e:
        print(f"An error occured: {e}")

