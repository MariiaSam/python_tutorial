'''
Каррінг (currying) — це техніка в програмуванні, коли функція, яка приймає кілька аргументів, перетворюється на послідовність функцій, кожна з яких приймає один аргумент. 
'''



def add(a):
    def add_b(b):
        return a + b 
    return add_b

# Використання:
add_5 = add(5)
result = add_5(10)
print(result)

# 15

#++++++++++++++++++++++++++++++++++++++ NOT CURRING
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)

# 450.0
# 400.0


from typing import Callable

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)

