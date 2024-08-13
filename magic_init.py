'''
Магічний метод __init__ не обов'язково повинен приймати аргументи та містити лише створення полів. Цей метод можна використовувати для реалізації будь-яких дій, які вам потрібні на етапі, коли об'єкт вже створений та його потрібно ініціалізувати.


'''


class Foo:
    def __init__(self, value=None):
        self.value = self.add_value(value)
        self.print_text()

    def print_text(self):
        print('print_text') # print_text

    def add_value(self, value):
        return value + 60

test = Foo(15)
print("1", test.value) # 75


#=========================================

class Phone:
    def __init__(self, value):
        if not self.phone_validation(value):
            raise ValueError

    def phone_validation(self, value):
        return len(value) == 10 and value.isnumeric()

phone = Phone('1234567890')

#=========================================


class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()  
        
        # Приклад логування
        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}")

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'

    def __check_adulthood(self) -> bool:
        return self.age >= 18

bill = Human('Bill')
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")

jill = Human('Jill', 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")


'''
Створено Human: Bill, Вік: 0, Дорослий: False
Hello! I am Bill
Вік: 0, Дорослий: False
Створено Human: Jill, Вік: 20, Дорослий: True
Hello! I am Jill
Вік: 20, Дорослий: True

'''