licznik = 0
with open("slowa.txt", "r") as plik:
    for linia in plik:
        slowo = linia.strip()
        for i in range(len(slowo) - 2 ):
            if slowo[i] == 'k' and slowo[i+2] == 't':
                licznik = 1 + licznik
                break

print(licznik)