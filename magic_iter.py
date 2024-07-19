'''
Створення об'єкта генератора/ітератора
Протокол ітератора в Python реалізовано за допомогою методу __iter__. Цей метод повинен повертати ітератор. Ітератором може бути будь-який об'єкт, у якого є метод __next__, який при кожному виклику повертає значення. Щоб створити ітератор, достатньо реалізувати метод __next__.
'''

class MultIterator:
    def __init__(self, seq, stop=1):
        self.seq = seq
        self.stop = stop
        self.loop = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop >= self.stop:
            raise StopIteration
        value = self.seq[self.idx]
        self.idx += 1
        if self.idx == len(self.seq):
            self.idx = 0
            self.loop += 1
        return value

seq = [1, 2, 3,4, True, None, 'test', 23]