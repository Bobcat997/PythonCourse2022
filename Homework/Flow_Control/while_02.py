secret_num = 11
while True:
    num = int(input("Podaj liczbę w przedziale od 1 - 20. "))
    if num != secret_num and num <= 20:
        print("Zgaduj dalej!")
    elif num > 20:
        print("To nie jest liczba od 1-20.")
    else:
        break
print("Gratulacje, zgadłeś!")