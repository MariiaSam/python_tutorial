'''
Метод get() використовується для безпечного отримання значення за ключем зі словника. Основна перевага цього методу полягає в тому, що він не викликає помилку, якщо ключ не знайдено. Натомість, якщо ключ відсутній, get() повертає None
'''


my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

'''
Коли ви використовуєте квадратні дужки [] для доступу до значення за ключем, отримаєте значення, якщо ключ існує. Проте, якщо ключ відсутній, Python викине помилку KeyError.


'''
my_dict = {"name": "Alice", "age": 25}
name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику
