'''
AND (і): Операція повертає True, якщо обидва операнди є True. Наприклад, True AND True є True, в той час як True AND False є False.

OR (або): Операція повертає True, якщо хоча б один з операндів є True. Наприклад, True OR False є True.

NOT (ні): Унарна операція, яка інвертує значення; True стає False, а False стає True.
'''

num = int(input("Введіть число: "))

length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парне двозначне число")
else:
    print("Ні")

#=======================
a = True or False  # True

#=======================

a = not 2 < 0  # True
