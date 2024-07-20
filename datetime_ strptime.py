'''
Метод strptime в Python використовується для перетворення рядків у об'єкти datetime
'''


# datetime_object = datetime.strptime(string, format)

'''
string - рядок, який містить дату та/або час.
format - рядок формату, який вказує, як розібрати string.
'''

from datetime import datetime

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
