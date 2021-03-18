Messsage = "Hail fellows well met, and welcome to the land of sanctity. Amongst all Ladies Lords and Knights we have lost a princess. Henceforth we ask of your intentions? is thou heart (G) Chivalrous or (D) Devilish? " 

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

def welcome_messsage():
    print("Welcome")

welcome_messsage()
print(demon_knight.hp)
demon_knight.attack()
print(demon_knight.hp)
