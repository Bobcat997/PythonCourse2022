# Love Calculator
# Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.

# Pobierz imiona zakochanych

# Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.

# Redukuj liczbę elementów tablicy dodając pierwszą i ostatnią liczbę do siebie, tak długo, aż zostną dwie cyfry.

# Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby.
import collections


def love_names():
    love1 = input("Podaj imię: ")
    love2 = input("Podaj imię: ")
    return love1 + love2


def count_words(love_names):
    word = love_names + 'love'
    return list(collections.Counter(word).values())


def reduce_list(l):
    new_list = []
    if l:
        if len(l) == 1:
            return l
        new_list.append(l[0] + l[-1])
        l.pop(0)
        l.pop(-1)
        new_list.extend(reduce_list(l))
    return new_list


def get_number(l):
    while len(l) > 2:
        l = reduce_list(l)
    return l


def main():
    l = count_words(love_names())
    number = get_number(l)
    print(f'Procent dopasowania wynosi: {number[0]}{number[1]}%')


main()