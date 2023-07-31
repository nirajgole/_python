class User:

    # count the number of users created
    # *It's a class variable/attributes
    active_users = 0

    @classmethod
    def total_active_users(cls):
        print(f"There are {cls.active_users} active users")

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))

    # *Constructor
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1

    # repr() is used to print the object in a readable format or simply it's just extra information about the object
    # ! If you don't define repr() it will print the object in a default format
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first_name} has logged out"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."

    def likes(self, thing):
        return f"{self.first_name} likes {thing}"

    def is_adult(self):
        return f'{self.first_name} is {"an adult" if self.age >= 18 else "not an adult"}'


# creating new user - John Smith
user1 = User('John', 'Smith', 30)

print(user1.first_name)
print(user1.initials())
print(user1.likes('ice cream'))
print(user1.is_adult())

# creating a new user - Jerry Smith
user2 = User('Jerry', 'Smith', 15)

print(user2.full_name())
print(user2.likes('ice cream'))
print(user2.is_adult())

# active users
print(User.active_users)
print(user2.logout())
print(User.active_users)

#class methods
User.total_active_users()
tom = User.from_string('Tom,Jones,89')
print(tom.full_name())

#Object/Class representation
jess = User('Jess', 'Smith', 25)
print(jess)
