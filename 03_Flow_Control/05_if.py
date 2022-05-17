# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

Password = input('Podaj hasło -->')
if len(Password) < 8:
    print('Hasło jest zbyt krótkie powinno zawierac 8 znaków')

if Password.isalnum() and Password.isdigit() or Password.isalpha():
    print('Hasło powinno zawierac litery i cyfry')

if Password.isalnum() and Password.islower():
    print('Hasło zawiera tylko małe litery, powinno zawierac conajmniej 1 duża litere')

if Password.isalnum() and Password.isupper():
    print('Hasło zawiera tylko duże litery, powinno zawierac conajmniej 1 małą litere')
