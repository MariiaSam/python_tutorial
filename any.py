
'''
Функція any() є вбудованою функцією, яка повертає True, якщо хоча б один елемент із заданого об'єкта ітерації є істинним. Якщо об'єкт ітерації порожній або всі його елементи є хибними, то any() повертає False.
'''

nums = [0, False, 5, 0]
result = any(nums)  
print(result)

# True


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)
# False