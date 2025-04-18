'''
Функція zip використовується для ітерації по декількох ітерованих об'єктах одночасно. Вона "застібає" елементи з кожного ітерованого об'єкта, створюючи кортежі з цих елементів.


'''

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

'''
зелене яблуко
стигла вишня
червоний томат
'''


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# =========================
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)

'''
1 a
2 b
3 c
'''