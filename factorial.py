'''
якщо n=0
 якщо n>0

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)
    
print(factorial(8)) # 40320
print(factorial(0)) # 1
print(factorial(3)) # 6

# =========================
def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
