x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50

'''
У Python кожна змінна, оголошена всередині функції, є локальною для цієї функції. Це означає, що локальні змінні існують лише в межах блоку коду, де вони були оголошені, і не доступні за його межами.


'''