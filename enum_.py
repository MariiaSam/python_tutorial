"""

https://uk.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%BB%D1%96%D1%87%D1%83%D0%B2%D0%B0%D0%BD%D0%B8%D0%B9_%D1%82%D0%B8%D0%BF_%D0%B4%D0%B0%D0%BD%D0%B8%D1%85

https://docs.python.org/3/library/enum.html

Enum, - це спосіб визначення набору іменованих констант у мовах програмування, що дозволяє використовувати більш зрозумілі імена для цих констант замість простих числових значень. Enum визначає символічні імена для набору пов'язаних значень, полегшуючи читання та розуміння коду.

Клас Enum з модуля enum дозволяє об'єднати ряд іменованих констант і гарантувати, що об'єкти цього класу можуть приймати тільки одне з обмежених значень, які вони описують.


"""

from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.") # Сьогодні понеділок.
else:
    print("Сьогодні не понеділок.") # 1

'''
Якщо у вас є значення і ви хочете отримати відповідний член Enum, ви можете використовувати метод Day() з цим значенням:


'''

day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY



from enum import Enum, auto

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")



order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()

Day.MONDAY
'''Сьогодні понеділок.
Статус замовлення 'Ноутбук': NEW.
Статус замовлення 'Книга': NEW.
Замовлення 'Ноутбук' оновлено до статусу PROCESSING.
Замовлення 'Книга' оновлено до статусу SHIPPED.
Статус замовлення 'Ноутбук': PROCESSING.
Статус замовлення 'Книга': SHIPPED.
'''
