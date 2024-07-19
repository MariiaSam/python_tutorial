'''
Множини — це неврегульований контейнер, який містить тільки унікальні елементи. У множину можна додавати тільки незмінні типи даних.


'''

empty_set = set()

a = set('hello')

b = {1, 2, 3, 4, 5}
#=================================
# c = set('dddd', 'ddd', 'dddddd')
# print(type(c))

''''  c = set('dddd', 'ddd', 'dddddd')
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: set expected at most 1 argument, got 3
'''

b = {'dddd', 'ddd', 'dddddd'}
print(type(b)) # set


numbers = {1, 2, 3, 1, 2, 3}
print(numbers) #{1, 2, 3}
