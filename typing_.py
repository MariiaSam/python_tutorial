'''
Оскільки такі об'єкти, як списки, словники та кортежі містять інші об'єкти, іноді нам потрібно ввести підказки, щоб зазначити, які типи об'єктів вони містять. Для цього нам потрібно звернутись до модуля typing, який надає інструменти для опису типів.



'''

from typing import List

Data = List[float | int]

def my_mul(data: Data) -> float:
    result = 1
    for num in data:
        result = result * num
    return result

my_mul([1, 2, 3])

#=================================

from typing import Dict

dict_of_users: Dict[int, str] = {
    1: "Jane",
    2: "Jon"
}

