import random
from enemy import Enemy

class Floor:
    # This class spawns enemies and controls their difficulty and gives players xp on floor completion
    def __init__(self, floor_number = None, mob_list = None):
        self.floor_number = 0 if floor_number is None else floor_number
        # Avoid using a mutable default argument so each Floor gets its own list
        self.mob_list = [] if mob_list is None else mob_list
    
    # GET FUNCTIONS
    def get_floor_number(self): # FLOOR NUMBER
        return self.floor_number
    
    def give_xp(self): # CALCULATES XP PER FLOOR
        # Calculate XP without modifying state; use base value of 20
        base_xp = 20
        calculated_xp = round(self.floor_number * 0.5 * base_xp) if self.floor_number > 1 else base_xp
        return calculated_xp
    
    def get_mob_list(self):
        return self.mob_list
    
    # SET FUNCTIONS
    # Sets mob list
    def spawn_mobs(self):
        # the amount of mobs spawned and their difficulty must follow the floor number
        # Floor 1-3 will have 2 enemies, 4-6 will have 3, and 7-9 will have 4, and floor 10 is a boss floor
        difficulty = self.floor_number
        mob_level = (difficulty+1)//2
        mob_health = (difficulty * 1.1) + 50
        mob_damage = (difficulty * 1.1) + 5
        mob_amount = ((difficulty+2)//3)
        
        if self.get_floor_number() != 10:
            for i in range(mob_amount+1):
                enemy = Enemy(Enemy.ENEMY_TYPES[random.randint(0,(len(Enemy.ENEMY_TYPES)-1))], round(mob_health), round(mob_damage), mob_level)
                #                           RANDOMIZED ENEMY TYPE                                         HEALTH       DAMAGE      LEVEL
                self.mob_list.append(enemy)
        else:
            enemy = Enemy("BOSS: Dragon",1000,50,10)
    
    def set_xp_given(self, xp_granted):
        self.xp_granted = xp_granted
    
    def __str__(self):
        return f"This is floor {self.get_floor_number()}. The enemies on this floor are {self.get_mob_list()}"