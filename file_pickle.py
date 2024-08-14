'''
Модуль pickle дозволяє серіалізувати об'єкти Python у потік байтів та десеріалізувати потік байтів назад у об'єкти. Це виправдано та корисно для зберігання об'єктів у файлах або передачі даних через мережу.

Основна мета pickle — зберегти стан об'єкта так, щоб його можна було точно відновити пізніше і часто в іншому місці.

Метод dumps запаковує в byte-рядок об'єкт, а метод loads потім розпаковує назад з byte-рядка в об'єкт

'''



'''
import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)  

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)
'''
