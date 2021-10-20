def citeste_numere_float():
    n = int(input("Introduceti numarul de elemente a listei: "))
    l = []
    for i in range(n):
        x = float(input("Introduceti un numar de tip float: "))
        l.append(x)
    return l


def afiseaza_partea_intreaga(lista):
    lista_intregi = []
    for num in lista:
        partea_intraga = int(num)
        lista_intregi.append(partea_intraga)
    print(lista_intregi)


def afiseaza_numere_din_interval(lista):
    n = float(input("Introduceti limita inferioara a intervalului: "))
    m = float(input("Introduceti limita superioara a intervalului: "))

    for num in lista:
        if n < num and num < m:
            print(num)

def afisare_numere_divizor(lista):
    for num in lista:
        numar_de_dupa_virgula = int(abs(num - int(num)) * 10)
        parte_intreaga = int(num)
        print(numar_de_dupa_virgula, parte_intreaga)
        if numar_de_dupa_virgula % parte_intreaga == 0:
            print(num)
    
    



info = """
Introduceti un numar corespunzator actiunii pe care doriti sa o efectuati:

1. Citeste lista de float
2. Afisarea partii intregi a tuturor numerelor din lista
3. Afisarea tuturor numerelor care apartin unui interval deschis citit de la tastatura
4. Afisarea tuturor numerelor a caror parte intreaga este divizor al partii fractionare
0. Iesire
"""

lista = None

while True:
    print(info)
    optiune = int(input("Introduceti un numar: "))

    if optiune == 1:
        lista = citeste_numere_float()
    elif optiune == 2:
        if lista == None:
            print("Lista dvs este vida")
            continue

        afiseaza_partea_intreaga(lista)
    elif optiune == 3:
        if lista == None:
            print("Lista dvs este vida")
            continue

        afiseaza_numere_din_interval(lista)
    elif optiune == 4:
        if lista == None:
            print("Lista dvs este vida")
            continue

        afisare_numere_divizor(lista)
    elif optiune == 0:
        break
    else:
        print("Introduceti un numar de la 0 la 4")



