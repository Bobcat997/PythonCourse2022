# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numbers = input("Podaj liczby podzielone przecinkiem")
numbers = numbers.split()
print(numbers)

print('Czy pierwszy i ostatni są takie same-->', numbers[0] == numbers[-1])
