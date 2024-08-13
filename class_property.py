'''
Гетери (від англ. get - отримувати) - це методи, які дозволяють отримати значення поля. Вони використовуються, коли доступ до поля потребує якоїсь додаткової обробки або коли безпосередній доступ до поля не бажаний з міркувань інкапсуляції. Наприклад, якщо потрібно завжди повертати значення поля у вигляді рядка, навіть якщо воно зберігається як число.

Сетери (від англ. set - встановлювати) - це методи, які дозволяють встановити значення поля. Вони найчастіше використовуються для валідації даних, які намагаються присвоїти полю. Наприклад, якщо ми маємо поле, який повинно приймати значення лише додатні числа, можна в сетері додати перевірку, яка буде викидати виняток або повертати помилку, якщо намагатися присвоїти йому від'ємне число.

Вбудований декоратор @property в Python дозволяє легко створювати гетери. Використання цього декоратора робить метод класу доступним як поле, тобто його можна буде викликати без дужок. Це робить інтерфейс класу більш чистим та інтуїтивно зрозумілим. Для створення сетера для того ж поля, що і гетер, використовується декоратор @property.setter, який застосовується до методу з тим же ім'ям, що і властивість.

'''

 
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name



# person = Person('Oleh', '23')

# print(person.get_name())
# person.set_name('Test')
# print(person.get_name())

# =====================================
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)


person = Person('Oleh', '23')

print(person.name)
person.name = 'Test'
print(person.name)

#=======================================

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

person = Person('Oleh', '23')

print(person.name)
person.name = 'Test'
print(person.name)

print(person.__dict__)