# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text1 = input("Wpisz Text-->")
text2 = " - "

for i in text1[1: :2]:
    text2 = text2 + i
print(text2)