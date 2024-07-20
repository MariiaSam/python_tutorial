'''
родовжує виконувати блок інструкцій, поки задана умова залишається істинною
'''
# k = 0
# while k < 10:
#     k = k + 1
# print(k)


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

'''
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
