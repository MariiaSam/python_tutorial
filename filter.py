# filter(function, iterable)

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums))

# [2, 4, 6, 8, 10]


def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))

# [1, 2]

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

# идавництво
