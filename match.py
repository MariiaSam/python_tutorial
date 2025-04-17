'''
match змінна:
    case шаблон1:
        # виконати код для шаблону 1
    case шаблон2:
        # виконати код для шаблону 2
    case _:
        # виконати код, якщо не знайдено відповідностей

'''

fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

#========================
pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.") # There's a dog.
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")

# ========================

a = 'Lev'

match a:
    case 'Jonh':
        print("This is Jonh")
    case 'Kate':
        print("This is Kate")
    case 'Kris':
        print("This is Kris")
    case 'Lev':
        print("This is Lev")
    case _:
        print("Unknown name")
        
# ========================

point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") # Точка лежить на осі X: x=1
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")
