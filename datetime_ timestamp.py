'''
термін timestamp (часова мітка) використовується для вказівки конкретного моменту в часі. Це зазвичай представляється як кількість секунд (або мілісекунд/мікросекунд у деяких системах) з певної початкової дати, найчастіше з 1 січня 1970 року в UTC, це часовий пояс Гринвіча.
'''

from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  #1721494987.840388


# Конвертація timestamp в об'єкт datetime


from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # 2021-03-31 12:40:00
