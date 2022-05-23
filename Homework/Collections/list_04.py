tab = []
num = int(input("Podaj parzystą ilośc elementow: "))
mid = int((num-1)/2)
if num % 2 == 0:
    for i in range(0,num):
        e = int(input("Podaj element-->"))
        tab.append(e)
    print(tab)
    if tab[mid] == tab[mid+1]:
        result = tab[mid]
        print(f"Są takie same o wartości {result}")
    else:
        print("Nie są takie same")
else:
    print("Miała być parzysta")