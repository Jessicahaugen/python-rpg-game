
Messsage = "Hail fellows well met, and welcome to the land of sanctity. Amongst all Ladies Lords and Knights we have lost a princess. Henceforth we ask of your intentions? is thou heart (G) Chivalrous or (D) Devilish? " 

import random

class Knight:
    def __init__(self, name, age, hp, items, spell):
        self.name = name
        self.age = age
        self.hp = hp
        self.items = items
        self.spell = spell
    
    def attack(self):
        self.hp -= 1000
        print("you have attacked")

    def spell(self):
        self.spell -= 100
        print(f"You have attacked with {self.spell}")


demon_knight = Knight("Demon Knight", 40, 1000, "Dark Excalibur", "a fireball")

holy_knight = Knight("Holy Knight", 20, 10000, "Light Excalibur", "divine light")

mage_knight = Knight("Mage Knight", 60, 1000, "Staff", "Fire Cast")

def welcome_messsage():
   
    print("""
“⚔️ Welcome young traveler! ⚔️
You’re about to fight the evil dragon. 
Good job! 
Choose your protagonist. 
Each one has different stats! Good luck!”
""")

welcome_messsage()

num1 = random.randint(1,20)

if num1 <= 5:
    demon_knight.attack()
elif num1 <= 7 and num1 > 5:
    demon_knight.attack()
elif num1 <= 10 and num1 > 7:
    demon_knight.attack()
elif num1 <= 14 and num1 > 10:
    demon_knight.attack()
elif num1 <= 16 and num1 > 14:
    demon_knight.attack()
elif num1 <= 20 and num1 > 17:
    demon_knight.attack()
else:
    print("Something is not right")

print(num1)


