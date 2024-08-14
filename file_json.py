'''
Модуль json перетворює dict в об’єкти JSON,
Список і кортеж перетворюються в масив JSON.
Рядок Python перетворюється на рядок JSON.
Цілі числа та дійсні числа перетворюються на числа JSON.
Логічне значення True перетворюється на константу JSON true.
Логічне значення False перетворюється на константу JSON false.
None перетворюється на константу JSON null.
'''

import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(json_string)
unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)

'''
{"key": "value", "2": [1, 2, 3], "my_tuple": [5, 6], "my_dict": {"key": "value"}}
{'key': 'value', '2': [1, 2, 3], 'my_tuple': [5, 6], 'my_dict': {'key': 'value'}}

'''
# https://s3.eu-north-1.amazonaws.com/lms.goit.files/f50750bb-6915-4e78-9238-55a11fe93c37Untitled%20-%202024-02-21T121058.758.png