'''
sorted() повертає новий відсортований об'єкт, залишаючи вихідний об'єкт без змін
'''

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]


'''Сортування у зворотному порядку:

'''
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

'''Сортування за довжиною:

'''
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']
