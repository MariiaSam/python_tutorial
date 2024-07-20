my_list = [1, 2, 3]
a, b, c = my_list

a, _, c = my_list

a, *rest = my_list

print(a) # 1
print(rest) # [2, 3]


#===================
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)
