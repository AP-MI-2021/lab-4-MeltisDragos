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


def medie_arit(l , x):
    '''
    !!!!!!!!!!!!!!!!!!!!!
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
                s = s + j
        rezultat.append(i)
        rezultat.append(s)
    return rezultat

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
        elif optiune  == "5":
            print(NrDivProprii(l))
        elif optiune == "x":
            break


main()