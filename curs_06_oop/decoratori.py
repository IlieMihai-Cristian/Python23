# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def change_name(self, name):
#         self.name = name
#         return self.name
#
#     @staticmethod
#     def bark():
#         return "ham, ham!"
#
# caine = Dog("Rex")
# print(caine)
# print(caine.change_name('Rex1'))
#
# # print(caine.bark(), Dog.bark())
# # print(caine.change_name('Rex2'), Dog.change_name('Rex3'))

# ---------------------------------------------------------------------------
# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property  #getter
#     def nume(self):
#         return self.__name
#
#     def __str__(self):
#         return self.__name
#
#
# caine = Dog("Rex")
# # print(caine._Dog__name)
# print(caine.nume)

# ---------------------------------------------------------------------------

# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property  #getter
#     def nume(self):
#         return self.__name
#
#     @nume.setter #setter
#     def nume(self, nume_schimbat):
#         self.__name = nume_schimbat
#
#     @nume.deleter  # setter
#     def nume(self):
#         del self.__name
#
#     def __str__(self):
#         return self.__name
#
# caine = Dog("Rex")
# # print(caine.nume)
# print(caine.__dict__, 'inainte de setter')
# caine.nume = "Max"
# # print(caine.nume)
# print(caine.__dict__, 'inainte de deleter')
# del caine.nume
# print(caine.__dict__, 'final')

# ---------------------------------------------------------------------------


# def decorator_simplu(parametru):
#     print(f'Apelam functia {parametru.__name__}')
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara!"
#
# print(functie_simpla())

# ---------------------------------------------------------------------------

# def decorator_depozit(functia_noastra):
#     def ambalaj(carte):
#         return f'Ambalare produs din {functia_noastra.__name__} ce contine cartea cu titlul {carte}'
#     return ambalaj
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume
#
# print(impachetare_carti('Moara cu noroc'))

# ---------------------------------------------------------------------------

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def interior_ambalaj(carte):
#             return (f'Ambalare produs din {functia_noastra.__name__} cu ambalaj din material {material} ce '
#                     f'contine cartea cu titlul {carte}')
#         return interior_ambalaj
#     return ambalaj
#
# # @decorator_depozit
# @decorator_depozit('hartie')
# def impachetare_carti(nume):
#     return nume
#
# print(impachetare_carti('Moara cu noroc'))

# ---------------------------------------------------------------------------

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def interior_ambalaj(*carte):
#             return (f'Ambalare produs din {functia_noastra.__name__} cu ambalaj din material {material} ce '
#                     f'contin cartile cu titlurile: {", ".join(carte)}')
#         return interior_ambalaj
#     return ambalaj
#
# # @decorator_depozit
# @decorator_depozit('hartie')
# def impachetare_carti(*nume):
#     return nume

# print(impachetare_carti('Moara cu noroc', 'Ion', 'Morometii'))

# ---------------------------------------------------------------------------

""" Ex: crearea unui decorator care sa converteasca sirul de caractere la litera mare"""

# def decorator(func):
#     def functie_upper(prop):
#         return prop.upper()
#     return functie_upper
#
# @decorator
# def my_function(propozitie):
#     return propozitie
#
#
# print(my_function('Ana are mere'))

# ---------------------------------------------------------------------------

# def decorator(semn):
#     def functia_noastra(func):
#         def functie_upper(prop):
#             if prop[-1] != semn:
#                 return prop.upper() + semn
#             return prop.upper()
#         return functie_upper
#     return functia_noastra
#
#
# @decorator("e")
# def my_function(propozitie):
#     return propozitie
#
#
# print(my_function('Ana are mere'))

# ---------------------------------------------------------------------------

import time

def execution_time(function_target):
    def wrapper(param):
        start = time.time()
        function_target(param)
        end = time.time()
        return f'Execution time: {end - start} and result is {function_target(param)}'
    return wrapper


@execution_time
def addition(number):
    initial_sum = 0
    for i in range(number):
        initial_sum += i
    return initial_sum

print(addition(10000000))

