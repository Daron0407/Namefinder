from lib.Multiset import Multiset
from collections import defaultdict
from sys import argv

SOURCES = r"./sources/"
PATH = r"./data/"

def main():
    text = "August Poniatowski"
    if len(argv) > 1:
        text = argv[1] + (argv[2] if len(argv) > 2 else '')
    text = text.lower().replace(' ','')
    Sext = Multiset(text)
    imiona = defaultdict(set)
    nazwiska = defaultdict(set)

    with open(SOURCES + "imionaM.txt", 'r', encoding ='utf8') as file:
        for imie in file:
            imie = imie.lower().strip()
            S = Multiset(imie)
            if Sext.subset(S):
                imiona[hash(S)].add(imie)


    with open(SOURCES + "imionaF.txt", 'r', encoding ='utf8') as file:
        for imie in file:
            imie = imie.lower().strip()
            S = Multiset(imie)
            if Sext.subset(S):
                imiona[hash(S)].add(imie)

    with open(SOURCES + "nazwiskaM.txt", 'r', encoding ='utf8') as file:
        for nazwisko in file:
            nazwisko = nazwisko.lower().strip()
            S = Multiset(nazwisko)
            if Sext.subset(S):
                nazwiska[hash(S)].add(nazwisko)


    with open(SOURCES + "nazwiskaF.txt", 'r', encoding ='utf8') as file:
        for nazwisko in file:
            nazwisko = nazwisko.lower().strip()
            S = Multiset(nazwisko)
            if Sext.subset(S):
                nazwiska[hash(S)].add(nazwisko)

    import os
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    total = 0
    with open(PATH + text + '.txt', 'w', encoding = 'utf8') as outputFile:
        for imieHash in imiona:
            for imie in imiona[imieHash]:
                rest = Sext - Multiset(imie)
                for nazwisko in nazwiska[hash(rest)]:
                    if sorted(imie + nazwisko) == sorted(text):
                        total += 1
                        outputFile.write(f"{imie} {nazwisko}\n")
    print(total)


if __name__=='__main__':
    main()