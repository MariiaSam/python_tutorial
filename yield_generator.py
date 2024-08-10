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

def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

# Використання генератора для читання рядків з файлу
for line in read_lines("my_file.txt"):
    print(line)



# Генератори можна перебирати в циклі for або вручну за допомогою функції next().

