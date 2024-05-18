class Person:

    def __init__(self,firs_name,last_name,age):
        self.first_name = firs_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be an integer')
        if value < 0 or value > 150:
            raise ValueError('age must between 0 and 150')
        self._age = value

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(' ')

jane = Person('Jane', 'Goodall', 50)
print(jane.age)
#calling setter
jane.age = 20
print(jane.age)
jane.full_name='John Doe'
print(jane.__dict__)