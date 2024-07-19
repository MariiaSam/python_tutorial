#  розширити один список іншим, то використовують метод extend

chars = ['a', 'b', 'c']
numbers = [1, 2]

chars.extend(numbers)

print(chars) # ['a', 'b', 'c', 1, 2]
