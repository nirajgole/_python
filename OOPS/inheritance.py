class Animal:
    cool = True

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f'This animal says {sound}')


class Cat(Animal):
    def __init__(self, name, breed, toy):
        # !super() is used to call the parent class
        super().__init__(name, species='Cat')
        self.breed = breed
        self.toy=toy

    def play(self):
        print(f'{self.name} plays with {self.toy}')


pussy = Cat('Pussy', 'Tabby', 'string') # !creating an instance of the Cat class
pussy.make_sound('meow')
# print(pussy.cool)
# print(Cat.cool)
# print(Animal.cool)
# print(isinstance(pussy, object))

pussy.play()

