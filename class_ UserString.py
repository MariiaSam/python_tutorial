from collections import UserString

# Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані лежать у полі data у цих класів і ви можете використовувати це поле на свій розсуд.


# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())


'''
Рядок: radar
Чи є паліндромом? True
Рядок: hello
Чи є паліндромом? False
'''


from collections import UserString

template = [
    "You can achieve anything. All it takes is a little effort and some books.",
    "This smartphone is the real deal. Big, bright screen, powerful processor, all in a small gadget.",
    "Collecting infinity stones is easy if you're a born hero.",
    "Mastering layout is easy. Pick up a new book and put all the exercises into practice.",
    "It's not hard to fight procrastination. Just take action. In small steps.",
    "Programming isn't as hard as they say.",
    "Simple daily exercises will help you succeed.",
]

class Comments(UserString):
    def get_limit_comment(self, max_len=15):
        return f"{self.data[:max_len-3]}..."

comments = [Comments(el) for el in template]


for comment in comments:
    # print(comment.get_limit_comment())
    print(comment.get_limit_comment(35))