'''
якщо n=0
 якщо n=1
 якщо n>1
​
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)
   
print(fibonacci(2)) # 1
print(fibonacci(1)) # 1
print(fibonacci(10)) # 55