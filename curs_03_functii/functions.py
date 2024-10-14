""" Definitia generala a functiilor """

# def nume_functie(parametru/parametrii):
#     set instructiuni

# def my_function():
#     var = 'orice'
#     return var
#
# func = my_function()
# print(func)

""" Parametrii si Argumentele functiilor """

def func(nume, cantitate, device):
    result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
    return result

# info = func('Mihai', 20, 'calculatoare')
# print(info)
# info2 = func('Adrian', 7, 'tablete', 'asdasd')

""" Argumente Keyword"""

# info_3 = func(device='telefoane', nume='Ana', cantitate=30)
# print(info_3)

# info_4 = func(device='a', nume='b', aaa=33)

# info_5 = func('Mihai', 10, device='baterii')

# info_5 = func('Mihai', cantitate=10, device='baterii')
# print(info_5)

info_6 = func('Mihai', device=10, cantitate='baterii')
print(info_6)