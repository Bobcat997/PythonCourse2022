# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

people = [
    ["Dorota", "Wellmann", "Dziennikarka"],
    ["Adam", "Małysz", "Sportoweic"],
    ["Robert", "Lewandowski", "Piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]

for person in people:
    for id, value in enumerate(person):
        if id == 1:
            print(value, end=":|",)
        else:
            print(value, end=" ")
    print()