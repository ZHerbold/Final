import random
class Enemy:
    # Enemy variables
    ENEMY_TYPES = ["Zombie", "Skeleton", "Slime", "Mimic", "Ghost", "Living Armor", "Goblin", "Orc", "Golem"]
    COMBAT_CLASSES = ["FIGHTER", "ROGUE", "MAGE", "CLERIC"]
    
    def __init__(self, combat_class = "No Class", type = "Unknown Monster", health = -1, max_health = -1, damage = -1, level = -1):
        self.type = type
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.level = level
        self.combat_class = combat_class
        self.heal_amount = 5 if self.combat_class == "CLERIC" else 0
        self.critical_chance = 0.5 if self.combat_class == "ROGUE" else 0.1

    # getter functions
    def get_type(self):
        return self.type

    def get_combat_class(self):
        return self.combat_class

    def get_health(self):
        return self.health
    
    def get_max_health(self):
        return self.max_health
    
    def get_damage(self):
        return self.damage
    
    def get_level(self):
        return self.level
    
    def get_critical_chance(self):
        return self.critical_chance
    
    def get_heal_amount(self):
        return self.heal_amount
    
    # setter functions
    def set_type(self, type):
        self.type = type

    def set_combat_class(self, combat_class):
        self.combat_class = combat_class
    
    def set_health(self, health):
        self.health = health

    def set_max_health(self, health):
        self.max_health = health

    def set_damage(self, damage):
        self.damage = damage
    
    def set_level(self, level):
        self.level = level

    # enemy functions
    def take_damage(self, damage_taken):
        health = self.get_health()
        health = health - damage_taken
        self.set_health(health)
    
    def heal(self, other):
        heal_amount = self.get_heal_amount()
        other.set_health(other.get_health() + heal_amount)
        if other.get_health() > other.get_max_health():
            other.set_health(other.get_max_health())
        print(f"The {self.get_type()} [{self.get_combat_class().lower()}] has just healed {other.get_type()} [{other.get_combat_class().lower()}] for {heal_amount} health points!")

    def attack(self, other):
        damage = random.randint(self.get_damage()-2,self.get_damage())
        critical_roll = random.uniform(0,1)
        is_critical = False
        if critical_roll < self.get_critical_chance():
            damage = round(damage * 1.5)
            is_critical = True
        other.take_damage(damage)
        crit_text = "CRITICAL HIT!" if is_critical == True else ""
        print(f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] has attacked the level {other.get_level()} player for {damage} health points! {crit_text}")
        
    def __str__(self):
        if self.get_health() > 0:
            return f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] has {self.get_health()}/{self.get_max_health()} health points left."
        else:
            return f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] is DEAD"
    
    def __repr__(self):
        return f"{self.get_combat_class()},{self.get_type()},{self.get_health()},{self.get_max_health()},{self.get_damage()},{self.get_level()}"