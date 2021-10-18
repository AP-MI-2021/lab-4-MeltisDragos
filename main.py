def citire_lista():
    l = []
    givenString = input("Dati numerele, separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def printMeniu():
    print("1.Cititi lista")
    print("2.Afisare lista")
    print("3.Elimina numerele prime din lista")
    print("4.Sa se afiseze daca media aritmetica a numerelor din lista este mai mare decat un numar dat")
    print("5.Sa se adauge numarul de divizori proprii dupa fiecare numar din fisier")
    print("6.")
    print("x.Iesire")


def NrPrim(a):
    '''
    Determina daca un numar este prim sau nu
    :param a: numar intreg
    :return: true sau false
    '''
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def test_NrPrim():
    assert(NrPrim(12)) is False
    assert(NrPrim(17)) is True


test_NrPrim()


def ElimNrPrim(l):
    '''
    elimina numerele prime din lista
    :param l: o lista de numere
    :return: lista fara numerele prime
    '''
    rezultat = []
    for i in l:
        if NrPrim(i) is False:
            rezultat.append(i)
    return rezultat


def test_ElimNrPrim():
    assert ElimNrPrim([12, 3, 13 , 24]) == [12, 24]


test_ElimNrPrim()


def medie_arit(l , x):
    '''
    se afiseze daca media aritmetica a numerelor din lista este mai mare decat un numar dat
    :param l: o lista de numere intregi
    :return: DA sau NU
    '''
    s = 0
    for i in l:
        s = s + i
    if s // len(l) > x:
        return True
    return False


def test_medie_arit():
    assert(medie_arit([12, 3, 4, 5], 4)) is True
    assert(medie_arit([12, 3, 4, 5], 20)) is False


test_medie_arit()


def NrDivProprii(l):
    '''
    adauga in lista duap fiecare elem numarul sau de div
    :param l: o lista de numere
    :return: lista
    '''
    rezultat = []
    for i in l:
        s = 0
        for j in range(2, i//2 + 1):
            if i % j ==0:
                s = s + 1
        rezultat.append(i)
        rezultat.append(s)
    return rezultat


def test_NrDivProprii():
    assert(NrDivProprii([12, 13, 14])) == [12, 4, 13, 0, 14, 2]


test_NrDivProprii()


def main():
    l = []
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(l)
        elif optiune == "3":
            print(ElimNrPrim(l))
        elif optiune == "4":
            print(NrDivProprii(l))
        elif optiune  == "5":
            print(NrDivProprii(l))
        elif optiune == "x":
            break


main()