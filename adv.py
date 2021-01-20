#OOP

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print("-----------------------------------------------------")
class BigObject:
    pass

obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(obj1))
print("-----------------------------------------------------")

#creating own objects

class PlayerCharacter:
    def __init__(self,name):
        self.name = name         #name - attribute,self - keyword,self refers player1 object
    def run(self):
        print("run")
player1 = PlayerCharacter("Agi")
print(player1)
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name):
        self.name = name         #attribute
    def run(self):
        print("run")
player1 = PlayerCharacter("Agi")
print(player1.name)
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name):
        self.name = name         #attribute
    def run(self):
        print("run")
player1 = PlayerCharacter("Agi")
player2 = PlayerCharacter("Pree")
print(player1.name)
print(player2.name)
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name         #attribute
        self.age = age
    def run(self):
        print("run")
player1 = PlayerCharacter("Agi",22)
player2 = PlayerCharacter("Pree",20)
print(player1.age)
print(player2.age)
print(player1.run)
print(player1.run())
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name         #attribute
        self.age = age
    def run(self):
        print("run")
        return 'done'
player1 = PlayerCharacter("Agi",22)
player2 = PlayerCharacter("Pree",20)
print(player1.run())
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name         #attribute
        self.age = age
    def run(self):
        print("run")
        return 'done'
player1 = PlayerCharacter("Agi",22)
player2 = PlayerCharacter("Pree",20)
print(player1)
print(player2)
print("-----------------------------------------------------")
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name         #attribute
        self.age = age
    def run(self):
        print("run")
        return 'done'
player1 = PlayerCharacter("Agi",22)
player2 = PlayerCharacter("Pree",20)
player2.attack = 50             # attack - attribute
print(player2.attack)
print("-----------------------------------------------------")

#attributes and methods

