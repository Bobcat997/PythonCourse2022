# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

user = []

repeated = {}
seen = set()

for i in range(5):
    l1 = []
    for j in range(4):
        l1.append(input(f'Podaj przedmiot dla usera {i}-->').lower())
    user.append(l1)
print(user)

for l in user:
  for item in set(l):
    if item in seen:
      if repeated.get(item):
        repeated[item] += 1
      else:
        repeated[item] = 2
    else:
      seen.add(item)

print(repeated)
print(max(repeated, key=repeated.get))