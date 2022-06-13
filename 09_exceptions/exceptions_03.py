# Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
# Obsłuż błędy.

def main():
    items = ['a', 'abc', 5, 5.0, [5, 3], (1, 3), 0, True, False, None, {}]


    try:
        id = int(input('Podaj index --> "'))
        print(1/ items[id])
    except ValueError as err:
        print('Value Error')
    except TypeError as err:
        print('Type error')
    except ZeroDivisionError:
        print('Cant divide by 0')
    except IndexError:
        print(f'You should give me lower value. 0 - {len(items)-1}')

if __name__== "__main__":
    main()