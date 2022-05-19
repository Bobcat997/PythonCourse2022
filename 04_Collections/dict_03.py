
n = int(input("Podaj liczbe od 1 do 10-->"))

tab = [['-'] *n] * n

for row in tab:
  for i in row:
      print(i, end=' ')
  print()