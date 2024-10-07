""" seturile sunt colectii de obiecte si sunt imutabile si neordonate (deci neindexabile). Nu permit elemente duplicate"""

var_set = set()
var_set1 = {1, "2", 3, "4", 1, 1, 1, "4", "2"}
# print(var_set1)
var_list1 = [1, "2", 3, "4", 1, 1, 1, "4", "2"]
# print(list(set(var_list1)))

""" pot contine elemente variate ( DOAR IMUTABILE)"""

var_set2 = {10, '22', 'abc', (1, 'x', 3)}
# print(var_set2)

""" dimensiunea unui set len()"""
# print(len(var_set2))

""" operatori in si not in """ # la fel ca la tupluri

""" operatii in seturi """

# var_set_a = {'a', 'b', 'c'}
# var_set_b = {'a', 'e', 'f'}

# UNION (preia toate elementele din operanzi fara duplicate)

# | (are nevoie doare de seturi), .union() (pot folosi si alte colectii iterabile)
# print(var_set_a | var_set_b)
# print(var_set_a.union(var_set_b))

# print(var_set_a | ('g', 'h', 'i'))
# print(var_set_a.union('g', 'h', 'i'))


# INTERSECTION (preia toate elementele comune)

# & (are nevoie doare de seturi), .intersection() (pot folosi si alte colectii iterabile)
# print(var_set_a & var_set_b)
# print(var_set_a.intersection(var_set_b))


# var_set_a = {'a', 'b', 'c'}
# var_set_b = {'a', 'e', 'f'}

# DIFFERENCE ()

# - (are nevoie doare de seturi), .difference() (pot folosi si alte colectii iterabile)
# print(var_set_a - var_set_b)
# print(var_set_a.difference(var_set_b))

# SYMMETRIC DIFFERENCE
# ^ (are nevoie doare de seturi), .symetric_difference() (pot folosi si alte colectii iterabile)
# print(var_set_a ^ var_set_b)
# print(var_set_a.symmetric_difference(var_set_b))

var_set_a = {'a', 'b', 'c'}
var_set_b = {'a', 'e', 'f'}

""" modificare seturi """
# update
# var_set_a.update(var_set_b)
# print(var_set_a)

# add
# var_set_a.add('d')
# print(var_set_a)

# remove
# var_set_a.remove('a')
# print(var_set_a)

# discard
# var_set_a.discard('x')
# print(var_set_a)

# pop
# var_set_a.pop()
# print(var_set_a)

# clear
# var_set_a.clear()
# print(var_set_a)