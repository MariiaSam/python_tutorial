my_dict = {}


my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# вивести значення
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

# змінити значення

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

'''Для перевірки, чи є ключ у словнику, використовуй оператор in:

'''

print("name" in my_dict)
print("age" in my_dict)

# ==============================

a = {'name': 'Mariia','name_2': 'Lev', 'city': 'New York', 'email': 'alice@example.com' }

del a["email"]
print(a) # {'name': 'Mariia', 'name_2': 'Lev', 'city': 'New York'}

a['name_3'] = 'Oleg'
print(a) # {'name': 'Mariia', 'name_2': 'Lev', 'city': 'New York', 'name_3': 'Oleg'}

a['name_3'] = 'Jon'
print(a) # {'name': 'Mariia', 'name_2': 'Lev', 'city': 'New York', 'name_3': 'Jon'}

print("email" in a) # False

# ==============================

b = {'name': 'Mariia','name_2': 'Lev', 'city': 'New York', 'email': 'alice@example.com' }

d = {}

for key in b:
    print(key)
'''
name
name_2
city
email
'''

for key in b:
    d[key] = b[key]
    print(d)

'''
{'name': 'Mariia'}
{'name': 'Mariia', 'name_2': 'Lev'}
{'name': 'Mariia', 'name_2': 'Lev', 'city': 'New York'}
{'name': 'Mariia', 'name_2': 'Lev', 'city': 'New York', 'email': 'alice@example.com'}
'''

# ==============================
for key, value in b.items():
    print(key, value)

'''
name Mariia
name_2 Lev
city New York
email alice@example.com
'''
