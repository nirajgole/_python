# polymorphism : The same method name is used for different types of objects.
# Example 1:
# len() is a method of str, tuple and list.

# Example 2:
# '+' is a method of int, float, complex and str.

#Example 3:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "woof!"


class Cat(Animal):
    def speak(self):
        return "meow!"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
print(f.speak())
