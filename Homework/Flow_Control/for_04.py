number = int(input("Podaj liczbę"))
if number < 9:
    silnia = 1
    for index in range(2, number+1):
        silnia = silnia * index

    print(silnia)
else:
    print("Nieprawidłowa liczba")