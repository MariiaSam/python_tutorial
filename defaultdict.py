'''Спеціальний словник defaultdict є підкласом словника dict у Python, який входить у модуль collections. Цей тип словника дозволяє призначити значення за замовчуванням для ключів, які ще не існують у словнику.

Під час створення defaultdict, ви повинні передати функцію, яка повертає значення за замовчуванням для нових ключів. Це може бути будь-який об'єкт, який може бути викликаний, наприклад, int, list, set або навіть ваша функція.


'''

from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

'''
defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
'''

d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)

'''defaultdict(<class 'int'>, {'a': 2, 'b': 1})
'''

from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))


'''
{
    'a': ['apple', 'appendix'],
    'z': ['zoo'],
    'l': ['lion', 'lama'],
    'b': ['bear', 'bet'],
    'w': ['wolf']
}

'''