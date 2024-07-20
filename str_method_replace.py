'''
Коли ж нам потрібно замінити деякий підрядок в рядку, ми можемо скористатися методом replace. Метод replace() у Python використовується для заміни підрядка на інший підрядок у рядку. Цей метод повертає новий рядок, де кожне входження вказаного підрядка замінено на інший підрядок
'''
# str.replace(old, new, count=-1)

'''
old - підрядок, який потрібно замінити.
new - підрядок, на який потрібно замінити.
count - лічильник максимальної кількості замін. Якщо не вказано або вказано -1, замінюються всі входження.
'''

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) # Hello Python


text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  # one bird, two bird, red fish, blue fish


'''!!!!!
Метод replace() також застосовують для видалення підрядка


'''

text = "Hello, world!"
new_text = text.replace(", world", "")
print(new_text) # Hello!
