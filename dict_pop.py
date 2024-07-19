'''
 pop(), який у словниках дозволяє видалити елемент за вказаним ключем і повернути його значення. 
'''

my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")
print(my_dict) # {'name': 'Alice'}
