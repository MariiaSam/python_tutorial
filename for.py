'''
У Python цикл for використовується для перебору усіх елементів контейнерів або ітерованих об'єктів, наприклад, списків. Інструкції, які знаходяться у тілі циклу, будуть виконані стільки разів, скільки елементів у колекції.


'''

fruit = 'apple'
for char in fruit:
    print(char)

'''
a
p
p
l
e
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")

'''
a b c d e f g h i j k l m n o p q r s t u v w x y z 
'''

some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)

'''
a
b
c

'''

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)
'''
1
9
25
49
81
'''

# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

# ========================

example = "Hello, World"
a = 1
y = 3

for i in example:
    if y <= a:
        print(i)
    else:
        print('No')
        
        '''
No
No
No
No
No
No
No
No
No
No
No
No
        
        '''
        
a_input = input("Input string: ") # Підрахунок загальної кількості символів та окремо кількості пробілів за допомоги циклу for та оператору if

total_c = len(a_input)
count = 0

for i in a_input:
    if i == " ":
        count +=1

print(f"Count of str {total_c}") # Count of str 106
print(f"Count of space {count}") # Count of space 14


# ========================

for i in range(0, 10, 2):
    print(i) 
    
''' 
0
2
4
6
8'''