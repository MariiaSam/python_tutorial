def a(numb_1: int, numb_2: int) -> int:
    sum = numb_1 + numb_2
    return sum 

x = 9
y = 12

a(x, y)

print(a(x, y)) # 21

# ==========================

def greet(name: str) -> str:
    return f"Hello, {name}"

name_greet = greet("Mariia")

print(name_greet) # Hello, Mariia

# ==========================

def if_true(numb: int) -> bool:
    return numb % 2 == 0


check_even = if_true(7)
print(check_even)  # False

check_even = if_true(10)
print(check_even)  # True

# ==========================

def string_to_codes(string: str) -> dict:
    codes = {}  
    for ch in string:  
        if ch not in codes:
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world!")
print(result)

{'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33}

# ==========================

x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50
