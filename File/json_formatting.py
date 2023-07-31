import json
# j = json.dumps({"name": "John", "age": 30, "city": "New York"}, indent=4)
# print(j)


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat('Garfield', 'Tabby')
j = json.dumps(c.__dict__)

print(j)
