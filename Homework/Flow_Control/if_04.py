# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

txt = "Pythaa"
if len(txt) > 5:
    if 'a' in txt:
        print(txt.replace('a', 'z'))
    print("Jest dłuższy niż 5 znaków")
else:
    print("Ma mniej niz 5 znaków")



