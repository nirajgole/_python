'''
scope - global, local
object - class, instance
'''

class Lion():
    name = 'Lion'
    type = "Carnivore"

    def __init__(self, name):
        self.name = name

leo = Lion('Leo')
print(Lion.name, leo.name, type(leo).name)

class Animal():
    name = None

animal_1 = Animal()
animal_1.name = 'Gazelle'
print(Animal.name, animal_1.name)
