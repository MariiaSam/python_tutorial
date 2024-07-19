
def print_text():
    print('Hello')

print_text()

class Product:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two

    def __call__(self):
        return self.value_one * self.value_two

product = Product(6, 6)

print(product())


#============================================

class Product:
    def __call__(self, value_one, value_two):
        return value_one * value_two

product = Product()

print(product(5, 9))


def class_decorator(cls):
    cls.magic_value = 40
    return cls
#============================================
@class_decorator
class Product:
    def __call__(self, value_one, value_two):
        return value_one * self.__divide(value_two)

    def __divide(self, value):
        print('Test data')
        return value / Product.magic_value

product = Product()

print(product(5, 9))
print(product.magic_value)

