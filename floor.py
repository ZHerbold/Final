import random
from enemy import Enemy

class Floor:
    # This class spawns enemies and controls their difficulty and gives players xp on floor completion
    def __init__(self, floor_number = 0, xp_granted = 20, mob_list = None):
        self.floor_number = floor_number
        self.xp_granted = xp_granted
        # Avoid using a mutable default argument so each Floor gets its own list
        self.mob_list = [] if mob_list is None else mob_list
    
    # GET FUNCTIONS
    def get_floor_number(self): # FLOOR NUMBER
        return self.floor_number
    
    def give_xp(self): # CALCULATES XP PER FLOOR
        self.xp_granted = round(self.floor_number * 0.5 * self.xp_granted) if self.floor_number > 1 else self.xp_granted
        return self.xp_granted
    
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
        
        for i in range(mob_amount+1):
            enemy = Enemy(Enemy.ENEMY_TYPES[random.randint(0,(len(Enemy.ENEMY_TYPES)-1))], round(mob_health), round(mob_damage), mob_level)
            #                           RANDOMIZED ENEMY TYPE                                         HEALTH       DAMAGE      LEVEL
            self.mob_list.append(enemy)
    
    def set_xp_given(self, xp_granted):
        self.xp_granted = xp_granted
    
    def __str__(self):
        return f"This is floor {self.get_floor_number()}. The enemies on this floor are {self.get_mob_list()}"