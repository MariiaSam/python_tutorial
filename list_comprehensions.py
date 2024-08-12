# [new_item for item in iterable if condition]


sq = [x**2 for x in range(1, 6)]
print(sq)

# Створення списку квадратів чисел від 1 до 5:

'''
[1, 4, 9, 16, 25]
'''

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)

# [4, 16, 36, 64]
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)

# [5, 7, 9]