'''
Модуль datetime надає зручні інструменти для роботи з датами та часом у форматі ISO 8601. Об'єкт datetime можна легко перетворити в рядок формату ISO 8601 за допомогою методу isoformat():
'''
from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format) # 2024-07-20T20:31:04.095134

'''
Метод isoformat() використовується для конвертації об'єкта datetime в рядок у форматі ISO 8601.
Метод fromisoformat() використовується для конвертації рядка у форматі ISO 8601 в об'єкт datetime.
Метод isoweekday() використовується для отримання дня тижня відповідно до ISO 8601.
Метод isocalendar() використовується для отримання кортежу, що містить ISO рік, номер тижня в році та номер дня тижня відповідно до ISO 8601.
'''