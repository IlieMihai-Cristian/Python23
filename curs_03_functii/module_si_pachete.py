# from fisier_exemplu_module import modul_func as my_func, var_ex as var
#
# print(my_func(1, 2, 3, 4, 5, 6, c=7, d=8, e=9))
# print(var)
# var_ex = 'altceva'
# print(var_ex)
import sys

# from fisier_exemplu_module import *
# import fisier_exemplu_module as x
# print(x.modul_func(1, 2, 3, 4, 5, 6, c=7, d=8, e=9))
# print(x.var_ex)

# print(x.__file__)
# print(dir(x))

# import curs_02_conditionari_si_loops.exemplu_fisier_pentru_pachete as pachet
# from curs_02_conditionari_si_loops.exemplu_fisier_pentru_pachete import modul_func
# print(pachet.modul_func(1, 2, 3, 4, 5, 6, c=7, d=8, e=9))

# print(sys.path)

# VAR 1:
# path_exemplu_pachet = '/home/mihai/SIIT/National-python23/curs_02_conditionari_si_loops'
# print(type(sys.path))
sys.path.append('/home/mihai/SIIT/National-python23/curs_02_conditionari_si_loops')
print(sys.path)

import curs_02_conditionari_si_loops.exemplu_fisier_pentru_pachete as pachet
# from curs_02_conditionari_si_loops.exemplu_fisier_pentru_pachete import modul_func
print(pachet.modul_func(1, 2, 3, 4, 5, 6, c=7, d=8, e=9))