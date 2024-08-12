# map(function, iterable, ...)

'''
Функція map() є функцією вищого порядку, що означає, що вона приймає іншу функцію як аргумент. map() використовується для застосування заданої функції до кожного елемента об'єкта ітерації, наприклад списку, та повертає ітератор, який виробляє результати.

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

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))
# [5, 7, 9]