'''
Якщо ми потребуємо саме округлення чисел, нам необхідно використовувати метод quantize. 
Наприклад, якщо ви хочете округлити число до двох знаків після коми, ви використовуєте Decimal об'єкт з двома нулями після коми як шаблон.
'''

from decimal import Decimal, ROUND_DOWN

# Вихідне число Decimal
number = Decimal('3.14159') # 3.14

# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

print(rounded_number)

'''

Округлення за замовчуванням ROUND_HALF_EVEN: 1.4
Округлення вгору ROUND_HALF_UP: 1.5
Округлення вниз ROUND_FLOOR: 1.4
Округлення вгору ROUND_CEILING: 1.5
Округлення до трьох десяткових знаків: 3.142

'''