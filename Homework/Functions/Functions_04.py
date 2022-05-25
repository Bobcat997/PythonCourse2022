# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
import random
def range(x,y,n):
    if n > x and n < y:
        print(f'tak, liczba {n} znajduje się w zadanym zakresie')
    else:
        print(f'nie, liczba {n} jest z poza zakresu')


def main():
    n = random.randint(1,100)
    x = int(input("Podaj zakres-->"))
    y = int(input("Podaj zakres-->"))
    range(x,y,n)


main()