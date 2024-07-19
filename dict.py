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