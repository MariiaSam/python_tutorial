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