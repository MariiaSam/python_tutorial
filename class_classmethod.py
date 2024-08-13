'''
Класові методи використовують декоратор @classmethod і, на відміну від статичних методів, мають доступ до самого класу через параметр cls, який автоматично передається Python. Це означає, що класові методи можуть змінювати стан класу або викликати інші класові методи. Класові методи часто використовуються для фабричних методів, які створюють екземпляри класу, використовуючи різні способи ініціалізації, ніж стандартний конструктор.
'''

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)

employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager
