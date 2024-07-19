'''
Він являється статичним методом і викликається при створені екземпляру класу.
 Потім вже метод `__init__()` ініціалізує цей екземпляр.
'''

class Foo:
    def __new__(cls, *args, **kwargs):
        print("Static method")
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value=None):
        print('Self constructor')
        self.value = value

test = Foo(134125235)
print(id(test))

test2 = Foo(134125235)
print(id(test2))