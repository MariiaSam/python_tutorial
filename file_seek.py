fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()

''''В цьому прикладі після запису у файл курсор буде зупинений на останньому символі. У виразі fh.seek(1) ми перемістили курсор на другий символ у файлі. '''