'''
Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні.


'''


import time

current_time = time.time()
print(f"Поточний час: {current_time}") # Поточний час: 1721497480.148582

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}") # Місцевий час: time.struct_time(tm_year=2024, tm_mon=7, tm_mday=20, tm_hour=20, tm_min=44, tm_sec=40, tm_wday=5, tm_yday=202, tm_isdst=1)
 