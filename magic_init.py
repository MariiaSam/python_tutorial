class Foo:
    def __init__(self, value=None):
        self.value = self.add_value(value)
        self.print_text()

    def print_text(self):
        print('print_text') # print_text

    def add_value(self, value):
        return value + 60

test = Foo(15)
print("1", test.value) # 75


#=========================================

class Phone:
    def __init__(self, value):
        if not self.phone_validation(value):
            raise ValueError

    def phone_validation(self, value):
        return len(value) == 10 and value.isnumeric()

phone = Phone('1234567890')