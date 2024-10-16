""" Declaratia IF """

# if expresie:
    # instructiune sau set de instructiuni

# first_number = 10
# second_number = 20

# if not first_number > second_number:
#     print('se respecta conditia')
# print('aici intra oricum')

first_number = 10
second_number = 20

# list_ex = ['rosu', 'galben', 'albastru']

# if 'galben' in list_ex:
#     print('expresia este adevarata') #1
#     if first_number > second_number:
#         print('a intrat pe primul if din interior expresie')
#     print('mesaj 1') #2
#     if first_number <= second_number:
#         print('a intrat pe al doilea if din expresie') #3
#     print('mesaj 2') #4
#     print('mesaj 3') #5
# print('mesaj 4') #6


""" conditiile elif si else """

# if expresie:
    # instructiune sau set de instructiuni
# else:
    # instructiune sau set de instructiuni

# var_nr = input(' Scrieti nr: ')
#
# if int(var_nr) >= 50:
#     print('nr este mai mare sau egal cu 50')
#     # print(f'Nr ales este: {var_nr}')
# else:
#     print('nr este mai mic decat 50')
# print(f'Nr ales este: {var_nr}')
#
#
# expression = False
# var_nr = 30
# if expression == True:
#     var_nr2 = 20

# elif -> else if

# nume = input('Alege un nume: ')
#
# if nume == 'Vlad':
#     print('Vlad')
# elif nume == 'George':
#     print('George')
# elif nume == 'Ana':
#     print('Ana')
# else:
#     print('Ai ales alt nume')


""" Operator Ternar """

# var = 'cuvant'
# val_ex = 10 if 'uv' in var else 20
# print(val_ex)

# if 'uv' in var:
#     val_ex = 10
# else:
#     val_ex = 20
# print(val_ex)

""" instructiunea PASS """

# if type(var) == 'str':
#     pass
# else:
#     var = 10


""" FOR LOOP """

# for <variabila temporara> in <iterabil>:
    # instructiune


# ex:1

# lista_ex = ['unu', 'doi', 'trei']
# for item in lista_ex:
#     print(item)

# ex:2

# var_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4}
# for x in var_dict:
#     print(x)
# for x in var_dict.keys():
#     print(x)

# for x in var_dict.values():
#     print(x)
# for x in var_dict:
#     print(var_dict[x])

# for key, value in var_dict.items():
#     print(f'Cheia: {key} -> are valoarea {value}')

""" FOR cu enumerate """
# lista_ex = ['unu', 'doi', 'trei']
# for idx, element in enumerate(lista_ex, start=100):
#     print(idx, ':', element)


""" FOR cu range """
# for item in range(-100, 100, 10):
#     print(item)
# print(list(range(2, 10)))


""" BREAK si CONTINUE """

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         continue
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         break
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         pass
#     print(animal)

""" FOR poate avea si ELSE """
# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     print(animal)
# else:
#     print('OK')


# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     print(animal)
#     break
# else:
#     print('OK')


""" WHILE LOOP """

# nr = 5
# while nr > 0:
#     nr -= 1
#     print(nr)

# animal = ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']
# while animal:
#     print(animal.pop(-1))

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         continue
#     print(nr)
# print('Final')

""" ELSE """
# nr = 5
# while nr > 0:
#     nr -= 1
#     print(nr)
# else:
#     print('Final')

# nr introdus de la tastatura
# calculam daca nr este pozitiv, negativ sau 0
# daca este pozitiv validam daca este mai mic ca 10 si afisam mesaj de confirmare
# daca este zero afisam ca nr este zero
# daca numarul este negativ afisam mesaj ca am introdus negativ si transformam in pozitiv

# user_input = input("Va rugam introduceti un nr.: ")
# # if user_input.isdigit():
# if user_input := int(user_input):
#     # user_input = int(user_input)
#     if user_input > 0:
#         if user_input < 10:
#             print(f'Nr este mai mic decat 10.\nNr ales este {user_input}')
#         else:
#             print(f'Nr este mai mare sau egal decat 10.\nNr ales este {user_input}')
#     elif user_input < 0:
#         print(f'Nr este mai mic decat 0.\nNr ales este {user_input}')
#         # print(f'Nr convertit pozitiv este {user_input*-1}')
#         print(abs(user_input))
#     else:
#         print('Numarul este 0')


""" DECLARATIA MATCH - CASE """

# ex:

car = 'BMWQ'

match car:
    case 'Audi' | 'BMW':
        print('German car')
    case 'Fiat':
        print('Italian car')
    case 'Toyota':
        print('Japanese car')
    case 'Dacia':
        print('Romanian car')
    case _:
        print('other car')

