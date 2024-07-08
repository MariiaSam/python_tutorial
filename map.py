# map(function, iterable, ...)

'''
function - функція, яку треба застосувати до кожного елемента в iterable.
iterable - об'єкт ітерації (список, кортеж тощо), елементи якого будуть оброблятися function.
'''

numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

'''
1
4
9
16
25


'''

numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

# [1, 4, 9, 16, 25]
