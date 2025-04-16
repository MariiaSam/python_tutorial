message = "Hello world!"

# 
s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2
print(joined_string)
# Hello world!


#===========================

name = "Oleg"
hello_string = f"Hello, {name}!"


# ==========================

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")

'''
\n - перенесення рядка
\f - перенесення сторінки
\r - перенесення каретки
\t - горизонтальна табуляція
\v - вертикальна табуляція

'''

print("Hello my little\rsister")

#===========================

example = "Hello, world!"

print(example[0]) # H
print(example[0:1]) # H
print(example[1:2]) # e
print(example[0:-1]) # Hello, world
print(example[-1]) # !
print(example[-2]) # d

example_1 = "Are you ready?"

example_2 = example + " " + example_1
print(example_2) # Hello, world! Are you ready?

print(f'{example}') # Hello, world!

