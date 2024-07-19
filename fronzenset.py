'''
Заморожені множини в Python, відомі як frozenset, є подібними до звичайних множин set, але з ключовою відмінністю: вони є незмінними. Це означає, що після створення замороженої множини ви не можете додати або видалити елементи з неї.

Заморожену множину можна створити за допомогою функції frozenset():


'''

my_frozenset = frozenset([1, 2, 3, 4, 5])

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})
