fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()

# ['first line\n', 'second line\n', 'third line']
#  який читає увесь файл повністю, але повертає список рядків, де елемент списку — це один рядок з файлу.