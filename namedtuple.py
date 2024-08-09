# Іменовані кортежі


from collections import namedtuple

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# Створення екземпляра Point
p = Point(11, y=22)

# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22

# ======================================

import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)       # Mick 
print(person.post_index) #01146
print(person.age)        # 35
print(person[3])       # Boston  

# ======================================
import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')
print(f'This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}')

'''
This is Simon, a 4-year-old cat. His owner is Krabat.

'''