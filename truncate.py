'''
Останній приклад показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів.


'''

from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts)

# hello w
