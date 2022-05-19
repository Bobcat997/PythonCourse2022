# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
number = int(input('Podaj liczbe od 1-8-->'))
if number < 9:
    silnia = 1
    for index in range(2, number+1):
        silnia = silnia * index
    print(silnia)
else:
    print("Nieprawidłowa liczba")