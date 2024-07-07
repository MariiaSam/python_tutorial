'''
Точність обчислень з Decimal контролюється через контекст. Можна налаштувати загальну точність для всіх обчислень Decimal.
'''

from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("1") / Decimal("7")) # 0.142857


getcontext().prec = 8
print(Decimal("1") / Decimal("7")) # 0.14285714

