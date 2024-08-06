'''
☝ Модуль shutil в Python - це модуль стандартної бібліотеки, який надає ряд функцій для роботи з файлами і колекціями файлів. Цей модуль може бути використаний для копіювання, переміщення, перейменування та видалення файлів і директорій, забезпечуючи високорівневі операції для обробки файлової системи, які є більш зручними, ніж використання базових функцій модуля os.

Пакет shutil підтримує архіви zip, tar, gz. Для цього він використовує пакети zipfile та tarfile. Ви можете використовувати їх напряму, якщо захочете.


shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
base_dir - директорія всередині архіву, з якої почнеться архівація.

'''
import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')
#=======================================================


'''shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією, файл буде скопійований зі своїм поточним іменем у цю директорію.
shutil.copytree(src, dst) рекурсивно копіює всю директорію src в директорію dst.
shutil.move(src, dst) переміщує файл або директорію src в dst.
shutil.rmtree(path) рекурсивно видаляє директорію path.
shutil.disk_usage(path) повертає статистику використання диска, що містить загальний об'єм, використаний об'єм і вільний об'єм для даного шляху.
'''
import shutil

shutil.unpack_archive(filename, extract_dir=None, format=None)

import shutil

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)
