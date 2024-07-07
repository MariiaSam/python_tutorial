'''
Замикання відбувається, коли внутрішня функція запам'ятовує стан свого оточення в момент свого створення і може використовувати ці змінні навіть після того, як зовнішня функція завершила своє виконання.
'''
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

# Hello, world!
