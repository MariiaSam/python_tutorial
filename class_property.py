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