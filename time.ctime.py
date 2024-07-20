'''
Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення. Якщо аргумент не вказаний, використовується поточний час.


'''

import time

current_time = time.time()
print(f"Поточний час: {current_time}") # Поточний час: 1721497412.8172631

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}") # Читабельний час: Sat Jul 20 20:43:32 2024