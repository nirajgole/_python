class User:
    def __init__(self, name=None):
        self.name = name
        print('A new user has been created!')


user1 = User("John")
user2 = User("Mary")
user3 = User()

# class variables types
#! python don't have private variables

class Person:
    def __init__(self):
        self.name = 'John'
        self._secret = 'It\'s a secret!'
        self.__age = 'Age is private!'

#python follows some conventions for naming variables
p = Person()
print(p.name)
# variable with single underscore is used to hide variables and should be used internally inside class only
print(p._secret)
#variable with double underscore is used to hide variables and should be used internally inside class only
#for this python internally do name mangling as _ClassName__variableName
print(p._Person__age)
print(dir(p))

#__method__ its a convention for python to know that this is dunder method or can be called magic method
# __init__ is a dunder method
