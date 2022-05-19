#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
#Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

num1 = float(input('Podaj Liczbe-->'))
num2 = float(input('Podaj Liczbe-->'))
result = num2 + num1
if result > 100:
    print('Wynik', result)
else:
    print('Koniec')