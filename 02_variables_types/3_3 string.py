# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

Palindrome = input('Podaj palindrom')

value = Palindrome.replace(" ", '').lower() == Palindrome.replace(" ", '').lower()[::-1]

print(f'is the {Palindrome.lower()} a palindrome-->', value)



