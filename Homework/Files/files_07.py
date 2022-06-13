import random

def category_pick():
  while True:
    choice = input("Wybierz kategorie. animals/flowers/fruits")
    if choice == "animals" or choice == "flowers" or choice == "fruits":
      with open(f"{choice}.txt", encoding="Utf-8") as fopen:
        content = fopen.readlines()
      break
    else:
      print("Wybierz z wybranych!!")
  return content


def computer_draw(content):

  computer_choice = random.choice(content)
  return computer_choice[:-1]


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
  content = category_pick()
  word = computer_draw(content)
  l = []
  guessed = False
  while attempt < 10:
    print(f'\n{mask_word(word, l)}\n')
    user_input = input('Enter a Letter: ').lower()
    if len(user_input) > 1:
      if user_input.lower() == word.lower():
        print('you guessed!')
        guessed = True
        break
    else:
      l.append(user_input)
    attempt += 1
  if not guessed:
    print(f'\n{mask_word(word, l)}\n')



main()
