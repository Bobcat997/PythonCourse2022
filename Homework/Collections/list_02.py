Lista = []
for i in range(0,10):
    num = int(input("Podaj liczby"))
    Lista.append(num)
print("Moje liczby:",Lista)


print("Liczby nieparzyste")
for i in Lista:
    if i % 2 != 0:
        print(i,end=" ")






