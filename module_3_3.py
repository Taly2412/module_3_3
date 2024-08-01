def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 'буква', False]
values_dict = {'a': 2, 'b': 'dog', 'c': 'cat'}
values_list_2 = [345, 'триста']

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
