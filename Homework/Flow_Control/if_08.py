# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

num1 = float(input('Podaj pierwszą liczbę-->'))
num2 = float(input('Podaj drugą liczbę-->'))
num3 = float(input('Podaj trzecią liczbę-->'))

if (num1 > num2) and (num1 > num3):
    maximum = num1
elif (num2 > num1) and (num2 > num3):
    maximum = num2
else:
    maximum = num3

print(maximum)

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
if num1 < num3:
    temp = num1
    num1 = num3
    num3 = temp
if num2 < num3:
    temp = num2
    num2 = num3
    num3 = temp
print(num1, num2, num3)
