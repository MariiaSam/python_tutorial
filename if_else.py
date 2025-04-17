x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")


a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')

# ==========================

a = 7

b = 89

c = 36

if c < b:
    print(f"Число {c} менше за {b}")
elif a < c and c <= b:
    print(f"Число {a} менше {b} і {c}")
else:
    print(7)
    