# Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

numbers = (1, 2, 3, 10, 20, 4, 5)
flag = False
num1 = input('Podaj cyfre')
for index, value in enumerate(numbers):
  if int(num1) == value:
      print("Znalazłem pod indexem", index)
      flag = True
      break

if not flag:
    print("Nie ma takiej liczby")