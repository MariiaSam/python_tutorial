'''
Перетин двох множин включає лише ті елементи, які є в обох множинах. Щоб знайти загальні елементи для двох множин, над ними треба виконати операцію & або використати метод intersection:


'''

a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))  # {3}
print(a & b)  # {3}
