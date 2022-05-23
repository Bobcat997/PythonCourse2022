a = 0
tuple1 = (5, 5, 5, 2, 2, 4, 4, 2, 5)
lista = list(tuple1)
print("Z Powtórzeniami-->",lista)
lista = sorted(lista)
for i in lista:
    a = lista.count(i)
    if a > 1:
        lista.remove(i)
tuple1 = tuple(lista)
print("Bez Powtórzeń-->",tuple1)