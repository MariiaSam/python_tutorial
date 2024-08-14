expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")

'''
Серіалізація об'єктів в Python — це процес перетворення структури даних або об'єкта в потік байтів для зберігання або передачі. Цей потік байтів може бути збережений у файлі, переданий через мережу або навіть використаний для зберігання в базі даних. Ціль серіалізації — зберегти стан об'єкта так, щоб його можна було відновити в майбутньому. Процес відновлення стану об'єкта з серіалізованої форми називається десеріалізацією.
'''

expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")
        
'''
Якщо потім знадобиться завантажити цей перелік назад у Python, завжди є змога це зробити:


'''

file_name = "expenses.txt"
expenses = {}

with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)

print(expenses)

# {'hotel': 150, 'breakfast': 30, 'taxi': 15, 'lunch': 20}
