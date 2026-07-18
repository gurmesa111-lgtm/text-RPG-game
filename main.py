from random import choice
# ======================================
# Text RPG Game Created by Gurmesa Borana
# A simple turn-based RPG built with Python.
# ======================================
# Player class
# Handles the player's stats, combat, inventory, shop, and level-up system.
class Player:
    def __init__(self, name, health = 100, attack = 20):
        self.name = name
        self.attack = attack
        self.max_health = health
        self.health = health
        self.xp = 0
        self.gold = 0
        self.h_potion = 3
        self.weapon = 'Wooden Sword'
        self.level = 1
        self.e_counter = 0

    # Display the player's current statistics
    def show_status(self):
        print("\n------Player Status------")
        print(f"\tName: {self.name.title()}"
              f"\n\tHealth: {self.health}/{self.max_health}"
              f"\n\tAttack: {self.attack}"
              f"\n\tExperience: {self.xp} XP"
              f"\n\tLevel: {self.level}")

    # Handle combat between the player and an enemy
    def attack_enemy(self, f_enemy):
        f_enemy.health -= self.attack
        print(f"\nYou attack the {f_enemy.name}!"
              f"\n{f_enemy.name} loses {self.attack} HP.")
        if f_enemy.health <= 0:
            self.e_counter += 1
            if f_enemy.name == 'Goblin':
                self.xp += 20
                self.gold += 20
                print("\n_______YOU WIN!_______"
                      "\nYou earned:"
                      "\n+20 XP"
                      "\n+20 Gold")
            elif f_enemy.name == 'Skeleton':
                self.xp += 35
                self.gold += 30
                print("\n_______YOU WIN!_______"
                      "\nYou earned:"
                      "\n+35 XP"
                      "\n+30 Gold")
            else:
                self.xp += 45
                self.gold += 40
                print("\n_______YOU WIN!_______"
                      "\nYou earned:"
                      "\n+45 XP"
                      "\n+40 Gold")
            self.level_up()
            return True
        self.health -= f_enemy.attack
        print(f"-----------------------"
              f"\n{f_enemy.name} attacks!"
              f"\nYou lose {f_enemy.attack} HP.")
        if self.health <= 0:
            print("\n_______YOU LOST!________\n"
                  "\n=============================="
                  "\n          Game Over!          "
                  "\n==============================\n"
                  f"\nThanks for playing, {self.name.title()}!\n"
                  f"\n\t     Final Statistics"
                  f"\n-----------------------------"
                  f"\nLevel: {self.level}"
                  f"\nXP: {self.xp}"
                  f"\nGold: {self.gold}"
                  f"\nWeapon: {self.weapon}"
                  f"\nEnemies Defeated: {self.e_counter}\n"
                  f"\nBetter luck next time!"
                  f"\n==============================")
            exit()
        return False

    # Display the inventory and allow the player to use health potions
    def inventory(self):
        while True:
            try:
                print("\n------Inventory------")
                print(f"Gold: {self.gold}"
                      f"\nHealth Potion: {self.h_potion}"
                      f"\nWeapon: {self.weapon}")
                print("\t1. Use Health Potion"
                      "\n\t2. Back")
                ch2 = int(input("Choice? "))
                if ch2 == 1 and self.h_potion >= 1 and self.health < self.max_health:
                    self.health += 30
                    self.h_potion -= 1
                    if self.health > self.max_health:
                        self.health = self.max_health
                    print(f"\n------------------------------"
                          f"\nYou used a Health Potion"
                          f"\nHealth: {self.health}/{self.max_health}"
                          f"\nHealth Potion left: {self.h_potion}"
                          f"\n------------------------------")
                elif ch2 == 1 and self.h_potion == 0:
                    print("\nNo Health Potion left to use!"
                          "\nVisit the shop to buy the health potion.")
                elif ch2 == 1 and self.h_potion > 0 and self.health == self.max_health:
                    print("\nYour health is already full.")
                elif ch2 == 2:
                    break
                else:
                    print("\nONLY SELECT ONE OF THE GIVEN OPTIONS!(1 or 2)")
            except ValueError:
                print("\nSELECT ONE OF THE GIVEN OPTIONS!")

    # Display the shop and allow the player to purchase weapons and health potions
    def shop_items(self):
        while True:
            try:
                print("\n------Weapon Shop------"
                      "\n1. Wooden Sword   - Free"
                      "\n2. Iron Sword     - 50 Gold"
                      "\n3. Steel Sword    - 100 Gold"
                      "\n4. Magic Sword    - 200 Gold"
                      "\n5. Health Potion  - 25 Gold"
                      "\n6. Exit Shop")
                ch1 = int(input("Choice? "))
                if ch1 == 1 and self.weapon == 'Wooden Sword':
                    print(f"You already own the {self.weapon}")
                elif ch1 == 1 and self.weapon in ['Iron Sword', 'Steel Sword', 'Magic Sword']:
                    print("\nYou can't downgrade a weapon!")
                elif ch1 in [1, 2] and self.weapon in ['Steel Sword', 'Magic Sword']:
                    print("\nYou can't downgrade a weapon!")
                elif ch1 in [1, 2, 3] and self.weapon == 'Magic Sword':
                    print("\nYou can't downgrade a weapon!")
                elif ch1 == 2 and self.weapon == 'Iron Sword':
                    print(f"You already own the {self.weapon}")
                elif ch1 == 2 and self.gold >= 50:
                    self.attack = 30
                    self.weapon = 'Iron Sword'
                    self.gold -= 50
                    print(f"\n------------------------------"
                          f"\nYou bought the Iron Sword!"
                          f"\nWeapon equipped: Iron sword"
                          f"\nAttack increased to {self.attack}."
                          f"\n------------------------------")
                elif ch1 == 2 and self.gold < 50:
                    print("\nNot enough gold.")
                elif ch1 == 3 and self.weapon == 'Steel Sword':
                    print(f"You already own the {self.weapon}")
                elif ch1 == 3 and self.gold >= 100:
                    self.attack = 40
                    self.weapon = 'Steel Sword'
                    self.gold -= 100
                    print(f"\n------------------------------"
                          f"\nYou bought the Steel Sword!"
                          f"\nWeapon equipped: Steel sword"
                          f"\nAttack increased to {self.attack}."
                          f"\n------------------------------")
                elif ch1 == 3 and self.gold < 100:
                    print("\nNot enough gold.")
                elif ch1 == 4 and self.weapon == 'Magic Sword':
                    print(f"You already own the {self.weapon}")
                elif ch1 == 4 and self.gold >= 200:
                    self.attack = 55
                    self.weapon = 'Magic Sword'
                    self.gold -= 200
                    print(f"\n------------------------------"
                          f"\nYou bought the Magic Sword!"
                          f"\nWeapon equipped: Magic sword"
                          f"\nAttack increased to {self.attack}."
                          f"\n------------------------------")
                elif ch1 == 4 and self.gold < 200:
                    print("\nNot enough gold.")
                elif ch1 == 5 and self.gold >= 25:
                    self.h_potion += 1
                    self.gold -= 25
                    print(f"\n------------------------------"
                          f"\nYou bought a health potion!"
                          f"\nHealth Potion: {self.h_potion}"
                          f"\nGold left: {self.gold}"
                          f"\n------------------------------")
                elif ch1 == 5 and self.gold < 25:
                    print("\nNot enough gold.")
                elif ch1 == 6:
                    break
                else:
                    print("\nONLY SELECT ONE OF THE GIVEN OPTIONS!(1 to 6)")
            except ValueError:
                print("\nSELECT ONE OF THE GIVEN OPTIONS!")

    # Increase the player's level and stats when enough XP has been earned
    def level_up(self):
        if self.xp >= 100 and self.level == 1:
            self.level += 1
            self.max_health = 110
            self.health = self.max_health
            print(f"\n========================"
                  f"\nLEVEL UP!"
                  f"\nYou reached Level {self.level}!\n"
                  f"\nMax Health +10\n"
                  f"\nHealth restored!"
                  f"\n========================\n")
        elif self.xp >= 250 and self.level == 2:
            self.level += 1
            self.max_health = 120
            self.health = self.max_health
            print(f"\n========================"
                  f"\nLEVEL UP!"
                  f"\nYou reached Level {self.level}!\n"
                  f"\nMax Health +10\n"
                  f"\nHealth restored!"
                  f"\n========================\n")
        elif self.xp >= 450 and self.level == 3:
            self.level += 1
            self.max_health = 130
            self.health = self.max_health
            print(f"\n========================"
                  f"\nLEVEL UP!"
                  f"\nYou reached Level {self.level}!\n"
                  f"\nMax Health +10\n"
                  f"\nHealth restored!"
                  f"\n========================\n")
        elif self.xp >= 700 and self.level == 4:
            self.level += 1
            self.max_health = 140
            self.health = self.max_health
            print(f"\n========================"
                  f"\nLEVEL UP!"
                  f"\nYou reached Level {self.level}!\n"
                  f"\nMax Health +10\n"
                  f"\nHealth restored!"
                  f"\n========================\n")

# Enemy class creates enemies with different stats.
class Enemy:
    def __init__(self):
        self.l_enemy = ['goblin', 'skeleton', 'orc']
        self.t_enemy = choice(self.l_enemy)
        print(f"{self.t_enemy.title()} appears.")
        if self.t_enemy == 'goblin':
            self.name = 'Goblin'
            self.health = 60
            self.attack = 10
        elif self.t_enemy == 'skeleton':
            self.name = 'Skeleton'
            self.health = 80
            self.attack = 15
        else:
            self.name = 'Orc'
            self.health = 100
            self.attack = 20
        self.max_health = self.health

    # Display the enemy's current statistics
    def show_status(self):
        print(f"\n------{self.t_enemy.title()} Status------")
        print(f"\tName: {self.name}"
              f"\n\tHealth: {self.health}/{self.max_health}"
              f"\n\tAttack: {self.attack}")

# Main Game
print("=================================="
      "\n              WELCOME             "
      "\n==================================")
p_name = input("Enter your name to start the game\n> ")
player = Player(p_name)
enemy = Enemy()
# Main game loop
while True:
    try:
        print("\n1. Attack"
              "\n2. View status"
              "\n3. Inventory"
              "\n4. Shop"
              "\n5. Quit")
        select = int(input("Enter your choice: "))
        if select == 1:
            value = player.attack_enemy(enemy)
            if value:
                print("\nA new enemy approaches!")
                enemy = Enemy()
        elif select == 2:
            while True:
                try:
                    print("\n\t1. Your status"
                          "\n\t2. Enemy's status"
                          "\n\t3. Back")
                    ch = int(input("\tChoice? "))
                    if ch == 1:
                        player.show_status()
                    elif ch == 2:
                        enemy.show_status()
                    elif ch == 3:
                        break
                    else:
                        print("\nONLY SELECT ONE OF THE GIVEN OPTIONS!(1 or 2)")
                except ValueError:
                    print("\nSELECT ONE OF THE GIVEN OPTIONS!")
        elif select == 3:
            player.inventory()
        elif select == 4:
            player.shop_items()
        elif select == 5:
            print("\nGOOD BYE!")
            break
        else:
            print("\nONLY SELECT ONE OF THE GIVEN OPTIONS!(1 to 5)")
    except ValueError:
        print("\nSELECT ONE OF THE GIVEN OPTIONS!")