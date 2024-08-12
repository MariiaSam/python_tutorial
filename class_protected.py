'''
Захищені (Protected) атрибути та методи.

Вони позначаються одним підкресленням _ на початку імені. Це лише конвенція, і захищені атрибути все ще можуть бути доступні ззовні, але це вважається поганою практикою змінювати їх ззовні.

Якщо ми хочемо взаємодіяти з захищеними полями об'єкту ззовні, необхідно впровадити правильний підхід до інкапсуляції у класі Person та слід використовувати методи для взаємодії з такими атрибутами об'єкту


'''


class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())
