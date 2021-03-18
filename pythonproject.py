Messsage = "Hail fellows well met, and welcome to the land of sanctity. Amongst all Ladies Lords and Knights we have lost a princess. Henceforth we ask of your intentions? is thou heart (G) Chivalrous or (D) Devilish? " 

class Knight:
    def __init__(self, name, hp, ap, spell, items):
        self.name = name
        self.ap = ap
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

def welcome_messsage():
    print("Welcome")

welcome_messsage()
print(demon_knight.hp)
demon_knight.attack()
print(demon_knight.hp)
