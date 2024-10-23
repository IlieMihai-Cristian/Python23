var = 10
# print(var/0)


""" Raise Exception """
# if var > 5:
#     raise Exception('Aici este o eroare')


""" Blocul try/except """

# ex:

# my_text = input('Introduceti un nr: ')
# try:
#     value = int(my_text)
#     print(value)
#     print(value2)
# except ValueError:
#     print("Nu pot converti acest sir de caractere")
# except NameError:
#     value2 = 100
#     print(f'Nu am gasit valoarea cautata asa ca alocam valoarea {value2}')
# except Exception as e:
#     print('intra pe exceptie ', e)


""" else si finally """

my_text = input('Introduceti un nr: ')
try:
    value = int(my_text)
    print(value)
    # print(value2)
except ValueError:
    print("Nu pot converti acest sir de caractere")
except NameError:
    value2 = 100
    print(f'Nu am gasit valoarea cautata asa ca alocam valoarea {value2}')
except Exception as e:
    print('intra pe exceptie ', e)
# else:
#     print('Nu sunt exceptii')
finally:
    print('Printeaza intotdeauna')
