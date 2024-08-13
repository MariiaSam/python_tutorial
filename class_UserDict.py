'''

Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані лежать у полі data у цих класів і ви можете використовувати це поле на свій розсуд.


UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника. Він дозволяє легше створювати власні класи словників, модифікуючи або додаючи нову поведінку до стандартних методів словника.


'''

from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)

# {'a': 1, 'b': 2, 'c': 3}


# =====================================

from collections import UserDict

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"

if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())

'''
{'a': 1, 'b': 2, 'c': 3}
---------------------------
Allen Raymond: (992) 914-3792
Chaim Lewis: (294) 840-6685
Kennedy Lane: (542) 451-7038
---------------------------
Allen Raymond: nulla.ante@vestibul.co.uk
Chaim Lewis: dui.in@egetlacus.ca
Kennedy Lane: mattis.Cras@nonenimMauris.net
'''