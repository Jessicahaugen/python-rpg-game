
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

        print(f"you have attacked and your hp has incresed 1000")

    def spell(self):
        self.ap += 1000
        print(f"You have attacked with {self.spell}")

    def item(self):
        self.hp += 3000
        print(f"your health has increased by 3000 and is now {self.hp}")
    
    


demon_knight = Knight("Demon Knight",1000, "Dark Excalibur", "devils blood")

holy_knight = Knight("Holy Knight", 10000, "Light Excalibur", "divine light")

mage_knight = Knight("Mage", 100000,20000,"Wrath of the Witch", "" )

dragon = Knight("Dragon",500000,40000,"Dragons Breath","Dragons Treasure" )


 

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


