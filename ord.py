'''
Функція ord() повертає цілочисельне представлення Unicode-символу. Наприклад:


'''

'''
Напишіть програму, щоб отримати ASCII значення введеного з клавіатури символа.

Вхідні дані:

G
w
+
Вихідні дані:

71
119
43
'''

def ascii_num(numb):
   total = ord(numb)
   print(total)


result = ascii_num('G')
result = ascii_num('w')
result = ascii_num('+')


'''
71
119
43
'''