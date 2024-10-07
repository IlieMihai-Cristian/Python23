""" dictionarele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile, incepand cu Python 3.7).
Nu permit elemente duplicate """

var_dict = {}
var_dict_a = dict()

var_dict_1 = {'cheie_1': 'valoare_1', 'cheie_2': 'valoare_2', 'cheie_3': 'valoare_3'}
# cheile sunt unice si imutabile
# dict_2 = {[1, 2]: 'aaaa'}
# print(dict_2)

""" lungime len() """ # la fel ca la restul

""" indexare """
# print(var_dict_1['cheie_2'])

""" dictionare intretesute """
ex_dict = {'key_1': {'key_2': {'key_3': ['a', 1.1, [333, (23, )]]}, 'key_4': 10}, 'key_5': 'key_6'}
# print(ex_dict['key_1']['key_2']['key_3'][2][1][0])
var_x = ex_dict['key_1']['key_2']['key_3'][1]
# print(var_x)

""" alocare elemente noi """
# var_dict_b = {'key_1': 1, 'key_2': 2}
# var_dict_b['key_2'] = 5
# print(var_dict_b)


""" cateva metode """
# clear
# var_dict_b.clear()
# print(var_dict_b)

# get
# print(var_dict_b['ionel'])
# print(var_dict_b.get('ionel', 100))

# items()
# print(var_dict_b.items())

# keys()
# print(var_dict_b.keys())

# values()
# print(var_dict_b.values())

var_dict_b = {'key_1': 1, 'key_2': 2, 'key_3': 3}

# pop()
# print(var_dict_b.pop('key_2'))
# print(var_dict_b)

# popitem()
# print(var_dict_b.popitem())
# print(var_dict_b)

# update()
var_dict_b.update({'key_5': 5})
print(var_dict_b)



