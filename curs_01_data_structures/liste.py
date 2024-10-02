""" listele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile). Permit elemente duplicate"""

# var_list = []
# var_list_a = list()

"""ordonare"""

# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]

# print(list_1 == list_2)
# print(list_1 is list_2)

""" pot contine o varietate de elemente"""
# list_var = [1, 2.5, 'aaa', False, None, len, int, [2, 3]]
# print(list_var)

""" concatenare  """
# print([1, 2] + [3, 4])

""" multiplicare"""
# print([1, 2] * 5)

""" lungimea len() """
# list_3 = [1, 4, 6, 8]
# print(len(list_3))

""" indexare """
# list_idx = [1, 2.5, 'aaa', False, None]
# print(list_idx[-1])

""" slicing """
# ca la stringuri
# print(list_idx[::-1])

""" copierea unei liste """
# list_4 = [1, 2.5, 'aaa', False, None]
# list_copy = list_4[:]
# print(list_4 is list_copy) # False

# list_copy = list_4.copy()
# print(list_4 is list_copy) # False

# list_copy = list_4
# # print(list_4 is list_copy)

""" operatori in si not in """
# ca la stringuri


""" liste intretesute (nested) """
# nested_list = ['1', [3, ['22', 16, None], ['mere', False]], [3.55], 0]
# print(nested_list[2][0])
# print(nested_list[1][1][2])

""" mutabilitate """
# list_5 = [1, 2.5, 'aaa', False, None]
# list_5[-2] = True
# print(list_5)

""" cateva metode folosite ptr obiecte de tip lista """
# count
list_m0 = [1, 3, 4, 7, 5, 1]
# print(list_m0.count(1))

# min si max
# list_m1 = [45, 10*23.2, 2, 78]
list_m1 = ['Ana', 'x', 'mihai', 'adi']
# print(max(list_m1))
# print(min(list_m1))

# stergere element
list_m2 = ['ana', 'are', 'mere', 'si', 'pere']
# del list_m2[-2]
# print(list_m2)

# modificarea unei liste
# - prin slice
# list_m2[1:2] = ['nu', 'are', 'fructele']
# print(list_m2)
# list_m2[:1] = ['razvan', 'si']
# print(list_m2)

# del list_m2
# print(list_m2)

# adaugare in lista
# cu append
# list_m3 = [1, 2.5, 'aaa', False, None]
# list_m3.append([3, 4])
# print(list_m3)
# list_m3 += ['ion']

# cu extend
# list_m3.extend(['ion', 'vlad'])
# print(list_m3)

# cu insert
# list_m3.insert(3, 'x')
# print(list_m3)


# remove
# list_m3.remove(2.5)
# print(list_m3)

# pop
# list_m3.pop(1)
# print(list_m3.pop())
# print(list_m3)

# clear
# list_m3.clear()
# print(list_m3)

# reverse
list_m3 = ['1', '2.5', 'Abc', 'False', 'None']
# list_m3.reverse()
# print(list_m3)

# sort
list_m3.sort(reverse=True)
print(list_m3)

var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
patches = [[4, 14, "Conquistador"], [25,31, "King"], [42, 49, "Palace"]]