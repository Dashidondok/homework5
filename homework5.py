immutable_var = 1, 2, 3, 'q', 'w'
print(immutable_var)
# immutable_var[0] = 100 # элементы кортежа неизменны, но есть исключение — если внутри кортежа находятся изменяемые элементы, например списки, то их значения можно изменить
mutable_list = [1, 2, 3, 'q', 'w']
mutable_list [0] = 4
mutable_list [1] = 5
mutable_list [2] = 6
mutable_list.append(False)
print(mutable_list)