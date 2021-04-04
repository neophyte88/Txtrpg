from random import randint # i use this a lot...like a lot a lot

class Character:
    #defining the Character class with basic attributes
    def __init__(self, powers, items=[]):
        self.hp = 35
        self.max_hp_level = 35 #added this to keep track of the max hp level for regen
        self.gold = 10
        self.level = 1
        self.exp = 0
        self.powers = powers
        self.equipment = {}
        self.items = items #add items with buffs and consumeables maybe??
        self.set_regen = False

    #define attack types
    def melee(self):
        if self.buff == 'Me':
            return randint(0, self.powers['melee']) + 5
        else:
            return randint(0, self.powers['melee'])
    def ranged(self):
        if self.buff == 'Ra':
            return randint(0, self.powers['ranged']) + 5
        else:
            return randint(0, self.powers['ranged'])

    def magic(self):
        if self.buff == 'Mag':
            return randint(0, self.powers['magic']) + 5
        else:
            return randint(0,self.powers['magic'])

    #level up and regen functions
    #level up gets called if the exp is high enough
    #regen is used with set regen to regenerate health after every step after a battle takes place

    def levelup(self):
        for power in self.powers:
            self.powers[power] += randint(1,10)
        self.hp += randint(5,10)
        self.level += 1
        self.exp = 0
    def regen(self):
        if hp >= max_hp_level:
            self.set_regen = False
        else:
            self.hp += 2

# the enemy class uses 2 lists and randint to decide what the name of the enemy will be
#no extra classification added yet

class Enemy:
    def __init__(self,playerlevel):
        self.names = ["Zombie",  "Wolf", "Necromancer", "Bandit", "Rouge", "Skeleton", "Orc", "Elf"]
        self.rarities = ["Common","Uncommon","Rare","Epic", "legendary"]
        if playerlevel <= 5:
            self.rarity = self.rarities[randint(0,1)]
            self.power = randint(1,10)
            self.hp = randint(5,15)
            self.drop_exp = randint(10,25)
        elif 5 < playerlevel <=10:
            self.rarity = self.rarities[randint(0,2)]
            self.power = randint(15,25)
            self.drop_exp = randint(20,35)
            self.hp = randint(15,35)
        elif 10 < playerlevel:
            self.rarity = self.rarities[randint(0,4)]
            self.power = randint(25,50)
            self.drop_exp = randint(35,45)
            self.hp = randint(20,50)
        self.name = self.rarity + " " +self.names[randint(0,7)]

    def attack(self):
        return randint(0,self.power)


#three base player classes that inherit the Character class
#need to add more to these....
#does nothing but assign some value to powers

class Knight(Character):
    def __init__(self,name):
        self.buff = 'Me'
        self.name = name
        self.powers = {
                'melee' : 15,
                'ranged': 5,
                'magic': 5,
        }
        super().__init__(self.powers)

class Archer(Character):
    def __init__(self,name):
        self.buff = 'Ra'
        self.name = name
        self.powers = {
                'melee' : 5 ,
                'ranged': 15,
                'magic': 5,
        }
        super().__init__(self.powers)

class Mage(Character):
    def __init__(self,name):
        self.buff = 'Mag'
        self.name = name
        self.powers = {
                'melee' : 5 ,
                'ranged': 5,
                'magic': 15,
        }
        super().__init__(self.powers)


#this is dead rn :\
class Item:
    def __init__(self):
        self.type = ' '
        self.name = ' '

def battle(enemy):
    print("---------------------------------------------")
    print(player.name , "VS" , enemy.name)
    print("your stats:-- hp:", player.hp, player.powers)
    print("enemies stats-- hp:", enemy.hp , " Attack power:" , enemy.hp )
    print("---------------------------------------------")
    #I KNOW THIS PART IS STUPID.....IDK what to do my head stopped working here
    #basically it has to go like ask me for attack - attack -- recive npc attack -- repeat if npc health > 0 and mine is > 0 too
    #need to improve
    battle_status = True
    outcome = ""
    while battle_status:
        if enemy.hp > 0 and player.hp > 0:
            att = int(input("Choose attack (1) Melee (2) Ranged (3) Magic \n"))
            if att == 1:
                dmg = player.melee()
                enemy.hp -= dmg
                print("You attacked " + enemy.name + " with " , dmg, " damage , Enemy HP :", enemy.hp )
            elif att == 2:
                dmg = player.ranged()
                enemy.hp -= dmg
                print("You attacked " + enemy.name + " with " , dmg, " damage , Enemy HP :", enemy.hp )
            elif att == 3:
                dmg = player.magic()
                enemy.hp -= dmg
                print("You attacked " + enemy.name + " with " , dmg, " damage , Enemy HP :", enemy.hp )

            else:
                print("Attack error!! You missed")
            if enemy.hp > 0:
                rcv_dmg = enemy.attack()
                player.hp -= rcv_dmg
                print(enemy.name + " Attacked you with ", rcv_dmg ," damage , Your HP :" , player.hp)

        elif player.hp <= 0:
            battle_status = False
            outcome = False

        else:
            battle_status = False
            outcome = True
    return outcome

def move():
    encounter = randint(0,30)
    if player.set_regen == True:
        player.regen()
    if player.exp >= 100:
        player.levelup()

    #idk why i used this to make a decision but it works so yay i guess
    if encounter % 3 == 0:
        enemy = Enemy(player.level)
        print("An " + enemy.name + " Approaches You")
        print("(1) Attack, (2) Run away")
        action = int(input(" what do you want to do \n"))
        if action == 2:
            print(" Congrats you ran away ")
            if player.gold != 0:
                player.gold -= round((player.gold/10))
                print(" Although you spilled some gold while doing so")
        elif action == 1:
            outcome = battle(enemy)
            if outcome == True:
                print("You won the battle!")
                print("---------------------------------------------")
                player.exp +=enemy.drop_exp
                player.regen_set = True
            elif outcome == False:
                print("You got defeated and lost a level and all your gold")
                player.level -= 1
                player.gold = 0
    else:
        print("Nothing fun happend, just like in real life")



# following is just to test the program....not the actual interface:
# i would put it in a main function but i just wanna see it run right now

print("Welcome!\n")
print("(1) New Game (2) Load (3) Exit ")

choice = int(input(""))

if choice == 1:
    choice = int(input("Pick a class (1)- knight, (2)- archer, (3)- mage \n"))


    if choice == 1:
        player = Knight(input("Enter a name for your knight \n"))
    elif choice == 2:
        player = Archer(input("Enter a name for your archer \n"))
    elif choice == 3:
        player = Mage(input("Enter a name for your Mage \n"))
    else:
        print("error!")
        exit()
elif choice == 3:
    exit()

print("Welcome Adventurer " + player.name+ "!")

while True:
    print("(1) Travel, (2) Exit")
    ACT = int(input(""))
    if ACT == 1:
        move()
    elif ACT == 2:
        exit()
    else:
        print("error")
