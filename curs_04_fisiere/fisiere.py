# read
# file = open('data.txt', 'r')

# write
# file = open('data.txt', 'w')
# file.write('Astazi este luni')
# file.close()

# append
# file = open('data.txt', 'a')
# file.write('Astazi este luni')
# file.close()

# read plus
# file = open('data.txt', 'r+')
# file.write('ABC')
# file.close()

"""
r (read)-> CITIRE DIN FISIER (daca fisierul nu exista, atunci cand am valoare r, o sa am eroare)
w (write)-> SCRIE IN FISIER (daca fisierul nu exista, atunci cand am valoare w, o sa creeze fisierul. Daca am ceva scris
                             in fiser, fct. write rescrie fisierul)
a (append)-> SCRIE IN FISIER (daca fisierul nu exista, atunci cand am valoare a, o sa creeze fisierul. Daca am ceva scris
                             in fiser, fct. append adauga la final de text)
r+ -> CITESTE SU SCRIE IN FISIER (daca fisierul nu exista, atunci cand am valoare r+, o sa am eroare. Daca exista ceva in
                                  fisier, scrie de la inceput peste ce exista deja)
"""
import csv

# file = open('data1.txt', 'w')
# try:
#     file.write('Astazi este luni')
# finally:
#     file.close()


""" declaratia "with" -> context manager """

# with open('data2.txt', 'w') as file:
#     file.write('Astazi este luni')

""" Citire din fisier """

# var 1
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# var 2
# with open('data.txt', 'r') as file:
#     # print(list(file))
#     for line in list(file):
#         print(line)

# var 3
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)


""" fisiere de tip CSV """

# with open('fisier_csv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     # print(type(rows))
#     for row in rows:
#         print(row)

""" adaugare rand/uri in csv """

car_list = [
    ['Dacia', 'Logan', 2015, 90],
    ['Renault', 'Clio', 2017, 115]
]

# with open('fisier_csv.csv', 'a') as csv_file:
#     csv_write = csv.writer(csv_file, delimiter=',')
#     csv_file.write('\n')
#     for car in car_list:
#         csv_write.writerow(car)

with open('fisier_csv.csv', 'a') as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',')
    csv_file.write('\n')
    csv_write.writerows(car_list)