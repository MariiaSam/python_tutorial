'''
Методи __getitem__ та __setitem__ в Python використовуються для налаштування доступу до елементів об'єкта за допомогою індексації або ключів, подібно до роботи зі списками чи словниками. Ці магічні методи дозволяють нашим класам імітувати контейнерні типи даних.


Метод __getitem__ визначає, як об'єкт класу повинен вести себе при доступі до його елементів за допомогою індексу або ключа. Він приймає ключ або індекс як аргумент і повинен повертати значення, асоційоване з цим ключем або індексом.


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

#=====================================