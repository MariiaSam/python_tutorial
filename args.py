'''
Параметр *args. Він дозволяє функції приймати довільну кількість позиційних аргументів. Аргументи, передані функції, зберігаються у вигляді кортежу.

'''

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)


'''
1
hello
True
'''

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

# Hello world!