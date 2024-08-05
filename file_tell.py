fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()

#Щоб дізнатися положення курсора в цей момент, можна скористатися методом tell, він повертає позицію (номер) символу з початку файлу, де зараз знаходиться курсор.


