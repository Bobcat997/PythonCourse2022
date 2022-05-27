# Stwórz grę wisielec “bez wisielca”.

# Komputer losuje wyraz z dostępnej w programie listy wyrazów.

# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)

# Użykownik podaje literę.

# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.

# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.

# Możesz ograniczyć liczbę prób do np. 10.
import random

words = ['python jest super', 'HTML to nie język programowania', 'Toyota to zabytkowy samochód']


def comp_choice(words):
  return random.choice(words)


def mask_word(word, letters):
  new_word = ''
  for letter in word:
    if letter.lower() in letters:
      new_word += letter
    else:
      if letter == ' ':
        new_word += ' '
      else:
        new_word += '-'
  return new_word

def main():
  attempt = 0
  word = comp_choice(words)
  l = []
  while attempt < 10:
    print(f'\n{mask_word(word, l)}\n')
    l.append(input('Podaj litere: ').lower())
    attempt += 1
  print(f'\n{mask_word(word, l)}\n')

main()