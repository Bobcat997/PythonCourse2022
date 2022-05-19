import random
words = [('kamien','nozyce'), ('papier','kamien'), ('nozyce', 'papier')]
num_of_rounds = int(input("Podaj liczbe rund--> "))

computer_wins = 0
user_wins = 0

for i in range(num_of_rounds):

    choice = input("Wybierz papier, kamien albo nożyce -> ")
    computer = random.choice(words)[0]
    if choice == computer:
        print("Remis, gracze wybrali to samo")
        continue
    for pair in words:
        if choice == pair[0] and computer == pair[1]:
            user_wins += 1
            draw = 0
            print("Gracz wygral runde")
            break
        elif choice == pair[1] and computer == pair[0]:
            computer_wins += 1
            draw = 0
            print("Komputer wygral runde")
            break

print()
print("-----------")
if user_wins > computer_wins:
    print("Gracz wygrał")
elif computer_wins > user_wins:
    print("Komputer wygral")
else:
    print("Remis")
