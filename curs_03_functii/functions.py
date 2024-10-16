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

# def func(nume, cantitate, device):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result

# info = func('Mihai', 20, 'calculatoare')
# print(info)
# info2 = func('Adrian', 7, 'tablete', 'asdasd')

""" Argumente Keyword(default)"""

# info_3 = func(device='telefoane', nume='Ana', cantitate=30)
# print(info_3)

# info_4 = func(device='a', nume='b', aaa=33)

# info_5 = func('Mihai', 10, device='baterii')

# info_5 = func('Mihai', cantitate=10, device='baterii')
# print(info_5)

# info_6 = func('Mihai', device=10, cantitate='baterii')
# print(info_6)


""" Parametrii Default(standard) """

# def func_2(nume="Radu", cantitate=100, device='ceasuri'):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result

# print(func_2())
# print(func_2('Ion', 50))
# print(func_2(cantitate=111))
# print(func_2('Alex', device='tablete'))


""" rezumat """

# CAZ 1: parametrii pozitionali: def func(a, b, c):

# 1. argumente pozitionale: func(10, 20, 30) -> conteaza atat ordinea cat si ca nr. de argumente = nr. de parametrii
# 2. argumente default: func(c=10, b=20, a=30) -> nu conteaza ordinea ci doar nr. de argumente = nr. de parametrii
# 3. argumente mix: func(10, c=20, b=30) -> pozitionale primele si keyword dupa + nr. de argumente = nr. de parametrii

# CAZ 2: parametrii default: def func(a=1, b=2, c=3):

# 1. argumente pozitionale: func(10, 20, 30) -> conteaza atat ordinea cat si ca nr. de argumente <= nr. de parametrii
# 2. argumente default: func(c=10, b=20, a=30) -> nu conteaza ordinea ci doar nr. de argumente <= nr. de parametrii
# 3. argumente mix: func(10, c=20, b=30) -> pozitionale primele si keyword dupa + nr. de argumente <= nr. de parametrii


# CAZ 3: parametrii mix: def func(a, b=2, c=3): # se respecta ordinea cu param. pozitionali primii
                                                # unde am param. pozitional se respecta regulile de la CAZ 1
                                                # unde am param. default se respecta de la CAZ 2


""" return """
# ex.

# def calc(x):
#     if x < 0:
#         return  # cand nu am valoare la return intotdeauna functia returneaza None
#     if x > 10:
#         return
#     print(x)  # cand nu am return intotdeauna functia returneaza None
#
#
# res = calc(-2)
# print(res)


""" ANOTARI """

# def calc(a: int = 1, b: int = 1, c: int = 1) -> int:
#     """
#     @:param a: aici introduci va
#     @:param b:
#     @:param c:
#     :rtype: object
#     """
#     return  a * b * c
#
# print('aaa')


""" args si kwargs """

# *args

# def suma(a, b=0, *args):
#     print(type(args)) # tuplu
#     print(args)
#     return a + b
#
# var = suma(1, 2, 3, 4, 5, 6)
# print(var)


# def suma(a, b=0, *gigel: int) -> int:
#     total = 0
#     initial = a + b
#     for x in gigel:
#         total += x
#     return initial + total
#
# var = suma(1, 2, 3, 4, 5, 6)
# print(var)


# **kwargs

# def suma(a, b=0, *args, **kwargs):
#     # print(type(kwargs)) # dict
#     # print(kwargs)
#     total = 0
#     initial = a + b
#     for x in args:
#         total += x
#     for y in kwargs.values():
#         total += y
#     return initial + total

# var = suma(1, 2, 3, 4, 5, 6, c=7, d=8, e=9)
# print(var)

# result = suma(1, 2, 3, c=7, d=8, e=9)
# result = suma(1, 2, c=7, d=8, e=9)
# result = suma(1, 2, 3, c=7, d=8, e=9, 4, 5)
# result = suma(3, 4, 5, d=8, e=9, a=1, b=2)
# result = suma(3, 4, 5, d=8, e=9, c=1, g=2)
# print(result)

""" RECURSIVITATE """

def test_func(nr):
    if nr > 100:
        return 101
    else:
        print(f'Nr este acum {nr}')
        return test_func(nr+10)

val = test_func(3)
print(val)

