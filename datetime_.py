''''
datetime.now(): Метод повертає об'єкт datetime, який містить поточну дату та час.
datetime.date(): Цей метод повертає об'єкт date, який представляє лише дату (без часу).
datetime.time(): Метод повертає об'єкт time, який містить лише час (без дати).
datetime.combine(date, time): Цей метод використовується для об'єднання об'єктів date та time і створення нового об'єкта datetime.
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Конструктор класу datetime дозволяє створити об'єкт datetime з конкретною датою та часом.
weekday(): Метод визначає номер дня тижня для вказаної дати, де понеділок має номер 0, а неділя - 6.

'''

import datetime

now = datetime.datetime.now()
print(now)

#2024-07-20 18:07:30.056551
'''
Для отримання поточної дати і часу використовується метод datetime.now():


'''

from datetime import datetime

current_datetime = datetime.now() # 2024-07-20 18:08:07.241951

print(current_datetime.year)  # 2024
print(current_datetime.month) # 7
print(current_datetime.day) # 20
print(current_datetime.hour) # 18 
print(current_datetime.minute) # 8
print(current_datetime.second) # 7
print(current_datetime.microsecond) # 242012
print(current_datetime.tzinfo) # None
 

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"
