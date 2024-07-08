'''
Функція all() є вбудованою функцією, яка повертає True, якщо всі елементи в переданому їй об'єкті ітерації є істинними - тобто не False, 0, "", None або будь-яке інше значення, яке Python оцінює як хибне. Але будьте уважні, якщо об'єкт ітерації порожній, функція all() повертає True.
'''

nums = [1, 2, 3, 4]
result = all(nums)  
print(result)

# True


words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)

# True
