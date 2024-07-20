'''
Є зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування об'єктів date та time. Це дозволяє створювати точний момент часу, вказуючи дату та час окремо, а потім об'єднуючи їх.


'''
# datetime.datetime.combine(date_object, time_object)

import datetime

# Створення об'єктів date і time
date_part = datetime.date(2024, 7, 20)
print(date_part) # 2024-07-20

time_part = datetime.time(12, 30, 15)
print(time_part) # 12:30:15

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part) # 2024-07-20 12:30:15

print(combined_datetime)  #  
