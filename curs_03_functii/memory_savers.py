""" Functia Lambda """  # (functie anonima)

# element = lambda x: x * 10
#
# def element_1(x):
#     return x * 10
#
# # print(element(10))
# # print(element_1(10))
#
# element_2 = lambda x, y: x + y
# print(element_2(11, 21))


""" FILTER """
# Fct. Filter intoarce un obiect al clasei filter (care este defapt un iterator) rezultat prin aplicarea unei functii
# fiecarui element dintr-un obiect iterabil (lista, tuplu .... )

# program care sa returneze o lista cu nr. pare dintr-o lista initiala data:

# list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]

# ex. 1:
# lista_noua = []
# for element in list_1:
#     if element % 2 == 0:
#         lista_noua.append(element)
# print(lista_noua)

# ex. 2:
# list_filter = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_filter)
# print(type(list_filter))
# print(list(list_filter))


# ex. 3:
# def filtrare(var):
#     if var % 2 == 0:
#         return True
#     else:
#         return False
#
# list_filter = list(filter(filtrare, list_1))
# print(list_filter)


""" MAP """
# Fct. MAP intoarce un obiect al clasei map (care este defapt un iterator) rezultat prin aplicarea unei functii
# fiecarui element dintr-un obiect iterabil (lista, tuplu .... )

# program care sa dubleze fiecare element dintr-o lista

# list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]
# list_map = list(map(lambda x: x * 2, list_1))
# print(list_map)


""" ZIP """
# Fct. ZIP preia parametrii iterabili (pot fi 0 sau mai multi) si returneaza un obiect al clasei zip sub forma de
# tupluri, formate din grupuri de elemente provenite din parametrii initiali.
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale

# list_with_int = [1, 2, 3, 4, 5, 6]
# list_with_str = ['one', 'two', 'three', 'four', 'five', 'six']
# list_with_decimals = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6']

# result = zip()
# var = list()
# var_2 = []
# print(list(zip(list_with_int, list_with_str, list_with_decimals)))
# print(dict(zip(list_with_int, list_with_str, list_with_decimals)))

""" UNZIP """
# res = zip(list_with_int, list_with_str, list_with_decimals)
# # print(list(res))
# val_1, val_2, val_3 = zip(*list(res))
# print(' val_1 = ', tuple(val_1))
# print(' val_2 = ', tuple(val_2))
# print(' val_3 = ', tuple(val_3))


""" COMPREHENSION LIST """

var = 'comprehension'

# # ex.1:
# print(list(var), 88)
#
# # ex.2 cu for:
# list_for_loop = []
# for letter in var:
#     list_for_loop.append(letter)
# print(list_for_loop, 94)
#
# # ex.3 cu lambda:
# print(list(map(lambda x: x, var)), 97)
#
# # ex.4 cu comprehension:
# list_comp = [letter for letter in var]
# print(list_comp, 101)

# nr_list = []
# for x in range(20):
#     if x % 2 == 0 and x % 5 == 0:
#         nr_list.append(x)
# print(nr_list)

# nr_list_2 = [x for x in range(20) if x % 2 == 0]   # lista_noua = [expresie(element) for iterabil if conditie]
# print(nr_list_2)
#
# nr_list_3 = [x for x in range(20) if x % 2 == 0 if x % 5 == 0]
# print(nr_list_3)

# nr_list_4 = [x for x in range(20) if x % 2 == 0 if x % 5 == 0]
#
# nr_list = []
# for x in range(20):
#     if x % 2 == 0:
#         nr_list.append('Par')
#     else:
#         nr_list.append('Impar')
# print(nr_list)
#
# nr_list_5 = ['Par' if x % 2 == 0 else 'Impar' for x in range(20)]
# print(nr_list_5)

""" COMPREHENSION DICTIONARY """

# square_dict = {}
# for num in range(1, 11):
#     square_dict[num] = num * num
# print(square_dict)
#
# square_comp = {num: num * num for num in range(1, 11)}
# print(square_comp)

a = [41, 42]
b = [1, 41]
c = [41, 45]

# # any()
# print(any(i in a for i in b))
# # all()
# print(all(i in a for i in c))

# value = 'a + 2'
# print(eval(value))

val_2 = '{1: 2}'
print(type(eval(val_2)))