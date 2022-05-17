sum_grades = 0
for i in range(3):
    subject = input("Podaj nazwe przedmiotu")
    grade = int(input(f'Podaj ocene z {subject}:'))
    print(f'ocena z {subject} to {grade}')
    sum_grades += grade
average = sum_grades/3
print(f'Twoja średnia ocen z 3 przedmiotów to {average} ')