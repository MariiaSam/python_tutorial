'''
Поліморфізм - це один із ключових концептів ООП, який дозволяє об'єктам мати різні форми або поведінку, базуючись на їх типах.

У контексті ООП, це відноситься до здатності різних класів використовувати методи з однаковою назвою, але з різною реалізацією. Це дозволяє використовувати один інтерфейс для різних типів даних.
'''

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)

'''
Тут make_sound - це метод, що використовується у кожному класі, але його реалізація різна для Cat та Dog. Це дозволяє нам викликати make_sound на екземплярі Animal, не знаючи точно, чи це Cat, Dog, чи інший підклас Animal. Ми створили функцію animal_sounds яка приймає список тварин і в принципі не важливо якого вони типу, головне, щоб вони реалізували метод make_sound:

Отже поліморфізм дозволяє обробляти об'єкти різних класів, які є похідними від одного базового класу, через спільний інтерфейс (тобто через однакові методи). 


'''


class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)

make_it_quack(person)

# Quack, quack!
# I'm Quacking Like a Duck!

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop

'''
Woof
Meow
Beep boop
'''