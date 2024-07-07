'''
Функції можуть бути аргументами інших функцій. Припустимо, у нас є декілька функцій для обчислення різних математичних операцій. Ми можемо створити функцію apply_operation, яка приймає іншу функцію, як аргумент та використовує її для обчислення результату.
'''

from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)

# 8, 15
