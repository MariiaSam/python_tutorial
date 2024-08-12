# lambda arguments: expression

print((lambda x, y: x + y)(5, 3))  # Виведе 8

# Тут lambda — це ключове слово, що вказує на початок лямбда-функції. arguments — це список аргументів, які приймає функція, а expression — це вираз, який буде виконано та його результат повернуто

nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)

# [5, 4, 3, 2, 1]