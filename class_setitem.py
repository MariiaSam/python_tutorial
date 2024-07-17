'''
Метод __setitem__ визначає, як об'єкт повинен поводити себе при присвоєнні значення елементу за певним індексом або ключем. Він приймає два аргументи: ключ (або індекс) та значення, яке потрібно асоціювати з цим ключем.


'''


class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age'])  
