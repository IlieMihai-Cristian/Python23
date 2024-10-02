""" siruri de caractere, imutabile si indexabile"""

# "programare"

var = str()

""" concatenare """

var_1 = 'pro'
var_2 = 'gram'
var_3 = 'are'

# print(var_1 + var_2 + var_3)

# 'aaaa'
# "aaaa"
# x = """Maria's toy"""
# print(x)

""" multiplicare """

# multip = 4
# print(multip * var_1, 'a')
# print(id(-4 * var_1))
# print(id(""))

""" transformare in string str()"""
# print(type(str(False)))

""" lungimea unui string len() """
# print(len(var_1))

""" operatori in si not in """
# print('gr' in var_2)
# print('gr' not in var_2)

""" indexare """ # var[index]
var_index = 'programare'
            #0123456789
# print(var_index[4])
# print(var_index[9])
# # print(var_index[10])
# print(var_index[-1])
# print(var_index[len(var_index)-1])
# print(var_index[-len(var_index)])

""" slicing """ # [start:stop:pasul]
# print(var_index[3:10:4])
# print(var_index[:5])
# print(var_index[::-1])

""" cateva metode folosite ptr obiectele de tip string """
# capitalize() - > primul char cu litera mare
# upper() - > toate char cu litera mare
# lower() - > toate char cu litera mica
# count(parametru) -> numara de cate ori gaseste parametru in string
# var_capital = var_index.capitalize()
# print(var_capital)
var_4 = 'Metoda folosita la stringuri'
# print(var_4.find('folosita')) # returneaza indexul primei echivalente gasite
# print(var_4.find('zzzzz')) # daca nu gaseste returneaza -1
# print(var_4.index('folosita')) # la fel ca metoda .find
# print(var_4.index('zzzzz')) # daca nu gaseste da eroare

var_5 = 'Ana are mere!'
# print(var_5.split()) # transforma un sire de caractere intr-o lista de substringuri
# print(var_5.replace('mere', 'pere'))

var_6 = '   programare   '
# print(var_6.lstrip())
# print(var_6.rstrip())
# print(var_6.strip())

var_7 = ['Ana', 'are', 'mere!']
# print(' '.join(var_7))



""" interpolare variabilelor la stringuri """

txt_1 = 'Python'
txt_2 = 'Scoala'
txt_3 = 'IT'

# caz 1 cu concatenare
# print('Grupa de ' + txt_1 + ' de la ' + txt_2 + ' Informala de ' + txt_3 + '!')

# caz 2 cu .format
    # cu acolade goale
# print('Grupa de {} de la {} Informala de {}!'.format(txt_1, txt_2, txt_3))
    # cu index in acolade
# print('Grupa de {0} de la {2} Informala de {1}!'.format(txt_1, txt_2, txt_3))
    # cu denumire variabila in acolade
# print('Grupa de {str_1} de la {str_2} Informala de {str_3}!'.format(str_1='Python', str_2='Scoala', str_3='IT'))

# caz 3 cu f- string
# print(f'Grupa de {txt_1} de la {txt_2} Informala de {txt_3}!')

# caz 4 varianta veche din Python 2.0
# print('Grupa de %s de la %s Informala de %s!' % (txt_1, txt_2, txt_3))