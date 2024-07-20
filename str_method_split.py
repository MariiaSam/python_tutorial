'''Метод split() у Python використовується для розбиття рядка на список підрядків на основі вказаного роздільника. Якщо роздільник не вказаний, за замовчуванням використовується пробіл.'''

# str.split(separator=None, maxsplit=-1)

'''
separator - роздільник, за яким слід розділяти рядок. Якщо не вказано, рядок розділяється за будь-яким пробілом.
maxsplit - максимальна кількість розділень. Значення -1 означає "без обмежень".
'''

# text = "hello world"
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']


text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']


result = '<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>'


