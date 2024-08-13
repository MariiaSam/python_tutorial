'''

Магічні методи __str__ та __repr__ в Python відіграють ключову роль у представленні об'єктів у вигляді рядків. Знання та правильне використання цих методів дозволяє контролювати, як об'єкти вашого класу відображаються і використовуються, що є важливою частиною розробки Python програм.

як об'єкт конвертується в рядок — це метод __str__. Коли ви викликаєте функцію str та передаєте їй якийсь об'єкт, то насправді цей об'єкт викликається магічним методом __str__

Наш метод __str__ призначений для повернення рядка, який є зрозумілим для кінцевого користувача. Якщо цей метод не визначено, Python використає метод __repr__ як запасний варіант для перетворення об'єкта в рядок.



'''

from datetime import datetime

test = datetime.now()

test_str = '12345'
test_list = [1, 2, 3]

print(str(test)) # 2024-05-13 20:15:18.596642
print(repr(test)) # datetime.datetime(2024, 5, 13, 20, 15, 18, 596642)

print(str(test_str)) # 12345
print(repr(test_str)) # '12345'

print(str(test_list)) # [1, 2, 3]
print(repr(test_list)) # [1, 2, 3]


print(test, test_str, test_list, sep='\n')

#============================================

class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __repr__(self):
        return f"{self.real} - {self.image}i"

    def __str__(self):
        return f"{self.real} + {self.image}i"



number = Complex(10, 20)
print(number)
print(str(number))

'''
10 + 20i
10 + 20i

'''

#===========================================


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print(human)

# Human named Alice who is 30 years old