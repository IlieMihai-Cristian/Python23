# Tom este o pisica mare care doarme toata ziua

# object_name = Tom (numele obiectului)
# class_name = Pisica (numele clasei)
# property = marime-pisica (proprietate sau atribut)
# activity = doarme

# O masina Dacia, merge repede

# object_name = Dacia
# class_name = masina
# property = repede
# activity = merge

# Catelul Dino are 4 picioare si latra tare

# object_name = Dino
# class_name = catel
# property =  4 picioare, tare
# activity = latra


# class Dog:
#
#     def __init__(self): # init
#         pass
#
#
# obj_1 = Dog()


# -------------------------------------------------

# stack_list = []
#
# def push(val):
#     stack_list.append(val)
#
# push(1)
# push(2)
# push(3)
#
# print(stack_list)
#
# def pop():
#     valoare = stack_list[-1]
#     del stack_list[-1]
#     return valoare
#
# print(pop())
# print(pop())
# print(pop())

# --------------------------------------------------------------

# class Stack:
#
#     def __init__(self):
#         # self.stack_list = []
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#
#     def pop(self):
#         variabila = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return variabila

# obj_stiva = Stack()
# # print(obj_stiva.stack_list)
# # print(obj_stiva.__stack_list)
# obj_stiva.push(1)
# obj_stiva.push(2)
# obj_stiva.push(3)
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())


# ------------------------------------------------------------------


# class Stack:
#
#     def __init__(self, val1):
#         self.__stack_list = []
#         self.valoare1 = val1
#
#     def push(self):
#         self.__stack_list.append(self.valoare1)
#
#     def pop(self):
#         variabila = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return variabila

# obj_stiva1 = Stack(1)
# obj_stiva2 = Stack(2)
# obj_stiva3 = Stack(3)
#
# obj_stiva1.push()
# obj_stiva2.push()
# obj_stiva3.push()
#
# print(obj_stiva1.pop())
# print(obj_stiva2.pop())
# print(obj_stiva3.pop())


# ----------------------------------------------------

class Stack:

    def __init__(self, *val1):
        self.__stack_list = []
        self.valoare1 = val1

    def push(self):
        for element in self.valoare1:
            self.__stack_list.append(element)
        print(self.__stack_list)

    def pop(self):
        variabila = self.__stack_list[-1]
        del self.__stack_list[-1]
        return variabila

obj_stiva = Stack(1, 2, 3)

obj_stiva.push()

print(obj_stiva.pop())
print(obj_stiva.pop())
print(obj_stiva.pop())