def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3


''' Коли функція викликає yield, вона "віддає" значення, яке слідує за yield, і "заморожує" свій поточний стан'''

def count_down(start):
    while start > 0:
        yield start
        start -= 1

for number in count_down(5):
    print(number)

'''
5
4
3
2
1
'''

