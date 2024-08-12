'''

 Атрибути, що вважаються приватними позначаються двома підкресленнями __ і не можуть бути доступні безпосередньо ззовні класу.
'''

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True, False)
# print(p.__is_admin)

'''

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[6], line 13
      9         return f"Hi {self.name}"
     12 p = Person("Boris", 34, True, False)
---> 13 print(p.__is_admin)

AttributeError: 'Person' object has no attribute '__is_admin'
'''

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p._Person__is_admin) # False
