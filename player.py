
import random

class Player:
    def __init__(self, xp_growth = 1.12):
        self.reset()
        self.xp_growth = xp_growth
        self.critical_chance = 0.25
    
    def reset(self):
        self.max_health = 100
        self.current_health = 100
        self.level = 1
        self.xp = 0
        self.max_xp = 80
        self.base_max_xp = self.max_xp
        self.equipment = {"Wooden Sword":1}
        self.currently_equipped = "Wooden Sword"
        self.damage = 10 * self.equipment[self.currently_equipped]

    # getter functions
    def get_max_health(self): # MAX HEALTH
        return self.max_health
    
    def get_current_health(self): # CURRENT HEALTH
        return self.current_health
    
    def get_xp(self): # XP
        return self.xp
    
    def get_max_xp(self): # XP THRESHOLD
        return self.max_xp
    
    def get_level(self): # LEVEL
        return self.level
    
    def get_damage(self): # DAMAGE
        return self.damage
    
    def get_equipment(self): # EQUIPMENT
        return self.equipment
    
    def get_currently_equipped(self):
        return self.currently_equipped
    
    def get_critical_chance(self):
        return self.critical_chance
    
    # setter functions
    def level_up(self):
        self.level += 1
        print(f"LEVEL UP! You are now level {self.get_level()}!")
        # Increase max health and damage on level up
        self.max_health = round(self.get_max_health() * 1.15)
        # Increase damage growth per level to 20%
        self.set_damage(round(self.get_damage() * 1.20))
    
    def set_damage(self, damage):
        self.damage = damage

    def set_equipment(self, equipment):
        self.equipment = equipment
    
    def raise_max_xp(self):
        # Recalculate max_xp using exponential growth from base_max_xp
        self.max_xp = round(self.base_max_xp * (self.xp_growth ** (self.level - 1)))

    def gain_experience(self, xp_gained):
        # Allow multiple level-ups from a single XP gain
        self.xp += xp_gained
        while self.xp >= self.max_xp:
            self.xp -= self.max_xp
            self.level_up()
            self.raise_max_xp()
    
    def set_current_health(self, health):
        self.current_health = health
    
    def load_save(self, max_health, current_health, max_damage, level, xp, max_xp, equipment, currently_equipped):
        self.max_health = max_health
        self.current_health = current_health
        self.damage = max_damage
        self.level = level
        self.xp = xp
        self.max_xp = max_xp
        self.equipment = equipment
        self.currently_equipped = currently_equipped

    # player functions
    def attack(self, other):
        damage = random.randint(self.get_damage()-2,self.get_damage())
        critical_roll = random.uniform(0,1)
        is_critical = False
        if critical_roll < self.get_critical_chance():
            damage = round(damage * 1.5)
            is_critical = True
        other.take_damage(damage)
        crit_text = "CRITICAL HIT!" if is_critical == True else ""
        print(f"You have attacked {other.get_type()} for {damage} damage! {crit_text}")
    
    def take_damage(self, damage):
        self.set_current_health(round(self.get_current_health() - damage))
    
    def heal(self):
        heal_amount = 50
        if (heal_amount + self.get_current_health() > self.get_max_health()):
            self.set_current_health(self.get_max_health())
        else:
            self.current_health += heal_amount

    def equip(self, equipment_name, multiplier):
        self.equipment[equipment_name] = multiplier
        self.damage = round(self.get_damage() * multiplier)
        self.currently_equipped = equipment_name

    def __str__(self):
        return f"PLAYER | HP {self.get_current_health()}/{self.get_max_health()} | LEVEL {self.get_level()} | XP {self.get_xp()}/{self.get_max_xp()} | EQUIPPED: {self.get_currently_equipped().upper()}"
    
    def __repr__(self):
        return f"{self.get_max_health()},{self.get_current_health()},{self.get_damage()},{self.get_level()},{self.get_xp()},{self.get_max_xp()},{self.get_equipment()},{self.get_currently_equipped()}"