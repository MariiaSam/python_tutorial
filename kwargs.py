'''
Параметр **kwargs використовується у визначенні функції для вказівки на те, що функція може приймати довільну кількість ключових аргументів. Назва kwargs пішла від "keyword arguments" та дозволяє передавати в функцію іменовані аргументи у вигляді словника.
'''

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)

'''
 name: Alice
age: 25
'''

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args) # Позиційні аргументи: (1, 2, 3)
    print("Ключові аргументи:", kwargs) # Позиційні аргументи: (1, 2, 3) Ключові аргументи: {'name': 'Alice', 'age': 25}

example_function(1, 2, 3, name="Alice", age=25)
