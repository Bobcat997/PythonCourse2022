#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
#Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
#Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinion = int(input('Podaj liczbe od 1-10'))
opinion2 = int(input('Podaj liczbe od 1-10'))
opinion3 = int(input('Podaj liczbe od 1-10'))
result = (opinion3 + opinion2 + opinion) / 3
if result > 7:
    print('Bardzo Dobry')
elif result >= 5:
    print('Przeciętna')
else:
    print('Nie warta uwagi')