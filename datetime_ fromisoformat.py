'''
Для зворотного перетворення рядка у форматі ISO 8601 на об'єкт datetime, можна використати метод fromisoformat():


'''

from datetime import datetime

iso_date_string = "2024-05-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso) # 2024-05-14 12:39:29.992996
