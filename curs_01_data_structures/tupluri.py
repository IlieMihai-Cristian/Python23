""" tuplurile sunt colectii de obiecte si sunt imutabile si ordonate (deci indexabile). Permit elemente duplicate"""

# var_list = ()
# var_list_a = tuple()

"""ordonare"""

# tuple_1 = (1, 2, 3, 4)
# tuple_2 = (1, 2, 3, 4)
#
# print(tuple_1 == tuple_2)
# print(tuple_1 is tuple_2)

""" pot contine o varietate de elemente"""  # la fel ca la liste

""" concatenare  """  # la fel ca la liste

""" multiplicare"""  # la fel ca la liste

""" lungimea len() """ # la fel ca la liste

""" indexare """ # la fel ca la liste

""" slicing """ # la fel ca la liste

""" copierea unui tuplu """ # metodele de copiere la fel ca la liste, doar cu valori True la comparare
# list_4 = (1, 2.5, 'aaa', False, None)
# list_copy = list_4[:]
# print(list_4 is list_copy) # True

# list_copy = list_4.copy()
# print(list_4 is list_copy) # True

# list_copy = list_4
# # print(list_4 is list_copy)

""" operatori in si not in """  # la fel ca la liste

""" tupluri intretesute (nested) """  # la fel ca la liste

""" metode tupluri """
# count
tuple_m0 = (1, 3, 4, 7, 5, 1)
# print(list_m0.count(1))

# index
tuple_m1 = (1, 3, 4, 7, 5, 1)
# print(tuple_m1.index(1))

# ((1, 'January'), (), ()
# ['aaaa']
tuple_1 = (2, )
# print(tuple_1, type(tuple_1))

# tuple_2 = (2, 4, 8)
# tupple_l = list(tuple_2)
# print(tupple_l, type(tupple_l))
# tupple_l.append(3)
# print(tupple_l, type(tupple_l))
# var = tuple(tupple_l)
# print(var, type(var))

list_ex = [1, 4, 6, 2, 7, 3, 8, 1111, 24324, 543634]
tuple_ex = (1, 4, 6, 2, 7, 3, 8, 1111, 24324, 543634)

import sys

print(sys.getsizeof(list_ex))
print(sys.getsizeof(tuple_ex))

