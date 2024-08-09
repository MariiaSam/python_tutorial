# Counter - це most_common(), який повертає список елементів та їх частоту

import collections

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

'''[(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
[(4, 4)]
[(4, 4), (6, 3)]
'''

#============================================
'''
Наприклад, якщо вам потрібно підрахувати кількість кожної літери у рядку, 
'''
from collections import Counter

# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count)

'''
Counter({'a': 3, 'n': 2, 'b': 1})
'''

#============================================

'''Виконати підрахунок слів в тексті теж стає досить простою задачею:
'''

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")


'''the: 2
quick: 1
brown: 1
fox: 1
jumps: 1
over: 1
lazy: 1
dog: 1'''


