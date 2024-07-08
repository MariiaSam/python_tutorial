'''
Замикання відбувається, коли внутрішня функція запам'ятовує стан свого оточення в момент свого створення і може використовувати ці змінні навіть після того, як зовнішня функція завершила своє виконання.
'''
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

# Hello, world!

'''
Внутрішня функція має доступ до змінних, визначених у області видимості зовнішньої функції.
Зовнішня функція повертає внутрішню функцію як результат своєї роботи.
Після завершення роботи зовнішньої функції, внутрішня функція зберігає доступ до цих змінних, що відіграє важливу роль у певних програмних патернах та алгоритмах.
'''

from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count

    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
