'''
Створення об'єкта генератора/ітератора
Протокол ітератора в Python реалізовано за допомогою методу __iter__. Цей метод повинен повертати ітератор. Ітератором може бути будь-який об'єкт, у якого є метод __next__, який при кожному виклику повертає значення. Щоб створити ітератор, достатньо реалізувати метод __next__.

Метод __iter__() повертає сам ітератор, а метод __next__() повертає наступний елемент об'єкта ітерації. Коли елементи ітератора закінчуються, має бути викинуто виняток StopIteration, що сигналізує про завершення ітерації.

Зверніть увагу, що метод __next__ повинен викликати виняток StopIteration, щоб вказати, що ітерування завершено, інакше цикл for за таким об'єктом буде нескінченний.




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

# =======================================

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current

if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)

'''
4
3
2
1
0
'''