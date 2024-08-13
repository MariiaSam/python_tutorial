'''
Метод __setitem__ визначає, як об'єкт повинен поводити себе при присвоєнні значення елементу за певним індексом або ключем. Він приймає два аргументи: ключ (або індекс) та значення, яке потрібно асоціювати з цим ключем.


'''

from collections import UserDict

class PositiveNumber(UserDict):

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]

    def __setitem__(self, key, value):
        if value > 0:
            self.data[key] = value


numbers=PositiveNumber()

numbers[3] = 1
numbers[1] = -3
numbers[None] = 5
numbers[2] = 7

print(numbers[2])
print(numbers)

#===============================

class PositiveNumber():

    def __init__(self, data=None):
        if data is None:
            self.data = dict()
        self.data = data

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]

    def __setitem__(self, key, value):
        if value > 0:
            self.data[key] = value

    def __str__(self):
        return f"{self.data}"


numbers=PositiveNumber()

numbers[3] = 1
numbers[1] = -3
numbers[None] = 5
numbers[2] = 7

print(numbers[2])
print(numbers)

#=============================================

class SimpleDict:
    def __init__(self):
        
        # У прикладі, SimpleDict використовує внутрішній приватний словник __data для зберігання своїх елементів. Метод __getitem__ дозволяє отримати значення за ключем, а __setitem__ – встановити нове значення для ключа.
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age'])  

'''

Boris
Key not found
'''