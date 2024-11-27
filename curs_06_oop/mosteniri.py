# class Example:
#
#     def __init__(self, val=1):
#         self.first = val
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second
#
#
# obj_1 = Example()
# print(obj_1)
#
# print(obj_1.set_second(4))
#
# print(obj_1.__dict__)
#
# obj_2 = Example(2)
# print(obj_2.__dict__)
#
# obj_2.third = 5
# print(obj_2.__dict__)

# -------------------------------------------------------------


# class Example:
#
#     def __init__(self, val=1):
#         self.__first = val
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second

# obj_1 = Example()
# print(obj_1.set_second(4))
# print(obj_1.__first)
# print(obj_1.__dict__)
# print(obj_1._Example__first)
# print(obj_1.__dir__())


# ---------------------------------------------------------------


# class Example:
#
#     __counter = 0 # proprietate a clasei
#
#     def __init__(self, val=1):
#         Example.__counter += 1
        # self.__counter += 1

# object_1 = Example()
# object_2 = Example(2)
# object_3 = Example(4)
#
# print(object_1.__dict__, object_1._Example__counter)
# print(object_2.__dict__, object_2._Example__counter)
# print(object_3.__dict__, object_3._Example__counter)


# ---------------------------------------------------------------

# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2

# object_1 = Example()
# print(hasattr(object_1, 'a'))
# print(hasattr(object_1, 'b'))
# print(object_1.b)


# -------------------------------------------------------------------

# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             Example.a = 10
#             self.a = 1
#         else:
#             self.b = 2
#
# object_1 = Example()
# print(object_1.__dict__) # propr. obiect
# print(Example.__dict__) # propr. clasa
#
# print(object_1.a)
# print(getattr(object_1, 'a'))


# -------------------------------------------------------------------

# class Example:
#
#     def __init__(self, val):
#         self.val = val
#
# ob1 = Example(0)
# ob2 = Example(2)
# ob3 = ob1
# ob3.val += 1
#
# print(ob1 is ob2)
# print(ob1 is ob3)
# print(ob1.val, ob2.val, ob3.val)


""" MOSTENIRI """


class Vehicule:
    pass


class Masini(Vehicule):
    pass


class MasiniDeTeren(Masini):
    pass

# print(issubclass(MasiniDeTeren, Vehicule))
# print(issubclass(Vehicule, MasiniDeTeren))

vehicul_1 = Vehicule()
masina_1 = Masini()
masina_de_teren_1 = MasiniDeTeren()

# print(isinstance(masina_1, MasiniDeTeren))
# print(isinstance(masina_1, Masini))
# print(isinstance(masina_1, Vehicule))


# class SuperClasa:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
# class SubClasa(SuperClasa):
#     def __init__(self, name):
#         # SuperClasa.__init__(self, name)
#         # super(SuperClasa, self).__init__(name)
#         super().__init__(name)
#
#     def __str__(self):
#         return f'Print {self.name}'
#
#
# object_1 = SubClasa('Mihai')
# print(object_1)

# -------------------------------------------------------------------


# class SuperClasa:
#     def __init__(self, name="Mihai"):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
# class SubClasa(SuperClasa):
#     def __init__(self, aaa="Ion"):
#         super().__init__(aaa)
#
#     def __str__(self):
#         return f'Print {self.name}'
#
#
# object_1 = SubClasa()
# print(object_1)


# -------------------------------------------------------------------


class SuperClasa:

    super_variabila = 'super'
    sub_variabila = 'sub_parinte'

    def __init__(self, name="Mihai"):
        self.name = name
        self.var_init = 30

    def __str__(self):
        return f'Numele meu este {self.name}'

class Mijloc:
    variabila_mijloc = 3
    super_variabila = 'mijloc'
    var_init = 50

class SubClasa(Mijloc, SuperClasa): # mostenire multipla

    sub_variabila = 'sub'
    super_variabila = 'super_copil'

    def __init__(self, aaa="Ion"):
        super().__init__(aaa)
        # self.var_init = 12

    def __str__(self):
        return f'Print {self.name}'

object_1 = SubClasa()
print(object_1.var_init)