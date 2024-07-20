'''Для пошуку деякого символу або підрядка у рядку можна скористатися методом find:'''

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1
