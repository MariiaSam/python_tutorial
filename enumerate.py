'''
Функція enumerate використовується для одночасного отримання індексу та значення елементів ітерованого об'єкта. Це корисно, коли вам потрібно отримати доступ до індексу елементів під час ітерації.


'''

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

'''
0 apple
1 banana
2 cherry
'''