'''
Метод join() у Python використовується для об'єднання послідовності рядків (наприклад, списку або кортежу) в один рядок з використанням вказаного роздільника. Цей метод викликається на рядковому об'єкті, який служить роздільником:
'''

'''
string.join(iterable)

string - рядок роздільник, який буде вставлений між елементами послідовності.
iterable - послідовність, список або кортеж рядків, які потрібно об'єднати.
'''

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'


elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'
