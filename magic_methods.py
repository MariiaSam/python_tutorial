'''

https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

 __init__(self) відповідає за ініціалізацію об'єкта

__len__(self) # Довжина

__getitem__(self, key) # Синатксис доступу за ключем (container[key])

__setitem__(self, key, value) # Синтаксис зміни за ключем (container[key] = new_value)

__delitem__(self, key) # Видалення елемента (del container[key])

__iter__(self) # Метод, який викликається функцією iter() або коли використовується `for ... in container:`

__reversed__(self) # Повертає container у зворотному порядку (якщо контейнер упорядкований)

__contains__(self, item) # Відповідає за синтаксис `some_val in container`

__missing__(self, key) # Відповідає за поведінку під час спроби звернутися до неіснуючого елемента'''