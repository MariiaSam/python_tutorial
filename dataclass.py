'''
Модуль dataclasses в Python надає засіб для декларативного визначення класів, які переважно використовуються

        для зберігання даних. 

Цей модуль введений у Python 3.7, щоб спростити створення таких класів без необхідності ручного написання бойлерплейт (від англ. - boilerplate) коду, який часто повторюється у традиційних класах.

☝ Використання @dataclass дозволяє зменшити кількість коду, необхідного для створення класів, які в основному зберігають дані. Це робить код більш читабельним і легшим для розуміння, а також автоматично створює конструктор класу __init__.



'''

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


# 

@dataclass
class Article:
    title: str
    author: str
    views: int = 0

# 
'''
Коли ми визначаємо клас Rectangle за допомогою @dataclass, Python автоматично створює метод __init__, який приймає атрибути width та height як параметри, за нас. Це означає, що нам не потрібно явно визначати конструктор класу.


'''

from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

'''
Тепер ми можемо створювати екземпляри класу Rectangle:
'''

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

'''
Кожен екземпляр класу Rectangle має метод area, який обчислює та повертає площу прямокутника, використовуючи атрибути width та height.


'''
print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")



"""Площа прямокутника 1: 50
Площа прямокутника 2: 21
Площа прямокутника 3: 48"""
