'''
Ми також можемо використовувати типи союзів Union. Наприклад, функція може повертати лише один з типів integer або float:


'''

from typing import Union

Number = Union[float, int]

def add(x: Number, y: Number) -> Number:
    return x + y

