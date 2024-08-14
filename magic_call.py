'''
☝ Функтори — це об'єкти, які поводяться як функції у тому сенсі, що їх можна викликати та передавати їм аргументи.

Функтори в Python — це об'єкти класів, які можуть бути викликані як функції. Це досягається за допомогою реалізації спеціального магічного методу __call__ для класу. Коли ви додаєте метод __call__ до класу, екземпляри цього класу можуть бути викликані звичайні функції.


'''

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other

# Створення екземпляра функтора
double = Multiplier(2)
triple = Multiplier(3)

# Виклик функтора
print(double(5))  # Виведе: 10
print(triple(3))  # Виведе: 9

#==========================================
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1

counter = Counter()
counter()
counter()
print(f"Викликано {counter.count} разів")
