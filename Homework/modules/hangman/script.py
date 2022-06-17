from hangman import words, comp_choice, mask_word

def main():
  attempt = 0
  word = comp_choice(words)
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