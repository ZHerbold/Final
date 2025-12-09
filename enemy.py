import random
class Enemy:
    # Enemy variables
    # Various types of enemies
    ENEMY_TYPES = ["Zombie", "Skeleton", "Slime", "Mimic", "Ghost", "Living Armor", "Goblin", "Orc", "Golem"]
    # Classes that determines the amount of damage and health an enemy has
    COMBAT_CLASSES = ["FIGHTER", "ROGUE", "MAGE", "CLERIC"]
    
    # initalizes a new enemy object
    def __init__(self, combat_class = "No Class", type = "Unknown Monster", health = -1, max_health = -1, damage = -1, level = -1):
        # sets various stats
        self.type = type
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.level = level
        self.combat_class = combat_class
        # sets the cleric healing amount to 5 and 0 for all other
        self.heal_amount = 5 if self.combat_class == "CLERIC" else 0
        # sets the critical chance of the rogue class to 50% and 10% for the rest of the classes
        self.critical_chance = 0.5 if self.combat_class == "ROGUE" else 0.1

    # getter functions
    def get_type(self): # TYPE
        return self.type

    def get_combat_class(self): # COMBAT CLASS
        return self.combat_class

    def get_health(self): # HEALTH
        return self.health
    
    def get_max_health(self): # MAX HEALTH
        return self.max_health
    
    def get_damage(self): # DAMAGE
        return self.damage
    
    def get_level(self): # LEVEL
        return self.level
    
    def get_critical_chance(self): # CRITICAL CHANCE
        return self.critical_chance
    
    def get_heal_amount(self): # HEAL AMOUNT
        return self.heal_amount
    
    # setter functions
    # sets the type of the enemy (species/kind)
    def set_type(self, type):
        self.type = type
    
    # sets the combat class of the enemy
    def set_combat_class(self, combat_class):
        self.combat_class = combat_class
    
    # sets the health of the enemy
    def set_health(self, health):
        self.health = health

    # sets the max health of the enemy
    def set_max_health(self, health):
        self.max_health = health

    # sets the damage of the enemy
    def set_damage(self, damage):
        self.damage = damage
    
    # sets the level of the enemy
    def set_level(self, level):
        self.level = level

    # enemy functions
    # This function lets the enemy take damage, it is called in the player's attack function
    def take_damage(self, damage_taken):
        # gets current health
        health = self.get_health()
        # subtracts the health by damage taken
        health = health - damage_taken
        # sets new health
        self.set_health(health)
    
    # this is the enemy cleric's heal function (supposed to be) that can heal any objects with the set and get health functions
    def heal(self, other):
        # gets the heal amount
        heal_amount = self.get_heal_amount()
        # increases the other's health by the heal amount
        other.set_health(other.get_health() + heal_amount)
        # checks if the health of the other enemy (or self) is greater than max
        if other.get_health() > other.get_max_health():
            # if so, sets to max so no overhealing
            other.set_health(other.get_max_health())
        # lets the player know that the cleric healed other enemies (or self)
        print(f"The {self.get_type()} [{self.get_combat_class().lower()}] has just healed {other.get_type()} [{other.get_combat_class().lower()}] for {heal_amount} health points!")

    # The enemy's attack function (pretty much exact the same as the player's attack function)
    def attack(self, other):
        # the damage is random from max damage - 2 to max damage (e.g., 4-6, 10-12, 100-102, etc.)
        damage = random.randint(self.get_damage()-2,self.get_damage())
        # rolls the critical chance roll from a float from 0 - 1
        critical_roll = random.uniform(0,1)
        # sets is critical to false (for text display reasons)
        is_critical = False
        # if the critical chance of the enemy is greater than or equal to the critical rolled, critical is true
        # example, critical roll is 0.64 but the enemy chance is 0.50 (rogue) or 0.10 (others), this means the crit failed
        # if roll is 0.15, then the crit succeed but only for the rogue
        # if roll is 0.09, then crit succeed for the rogue and all other classes
        if critical_roll < self.get_critical_chance():
            # critical damage is increased by 50%
            damage = round(damage * 1.5)
            # sets is critical to true
            is_critical = True
        # calls the other's take damage method (found in the player.py)
        other.take_damage(damage)
        # If the crit succeed, it will display CRITICAL HIT at the end of the print statement
        crit_text = "CRITICAL HIT!" if is_critical == True else ""
        # Lets the player know how much damage they took and by who
        print(f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] has attacked the level {other.get_level()} player for {damage} health points! {crit_text}")
    
    # string that lets player know the stats of the enemy
    def __str__(self):
        # checks if enemy is still alive and prints out stats
        if self.get_health() > 0:
            return f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] has {self.get_health()}/{self.get_max_health()} health points left."
        # if the enemy is dead, tell the player
        else:
            return f"Level {self.get_level()} {self.get_type()} [{self.get_combat_class().lower()}] is DEAD"
    
    # repr for saving to file purposes
    def __repr__(self):
        return f"{self.get_combat_class()},{self.get_type()},{self.get_health()},{self.get_max_health()},{self.get_damage()},{self.get_level()}"