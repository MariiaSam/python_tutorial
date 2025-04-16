a = [1, 3, "Hello", True, 10]

a.remove(True)

print(a) # [3, 'Hello', True, 10]

a.remove(10)
print(a)

a = [1, 3, "Hello", True, 10]

for index, item in enumerate(a):
    if item is True:
        a.pop(index)
        break

print(a) # [1, 3, 'Hello', 10]
