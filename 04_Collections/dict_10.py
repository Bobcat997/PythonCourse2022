#Użytkownik podaje dowolną liczbę N.
#Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
#Załóżmy, że użytkownik podał N = 8
#Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input('Podaj liczbę od 1-10-->'))

dict_sqr = {}
for v in range(1,n + 1):
    dict_sqr[v] = v * v

print(dict_sqr)
