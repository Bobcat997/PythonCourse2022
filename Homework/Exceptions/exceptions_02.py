
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
def get_user_data():
    user1 = input(f'Podaj index wartości do zmiany, z zakresu od 0 do {len(tuple1) - 1} -> ')
    user_value = input(f'Podaj nową wartość elementu o indeksie {user1} -> ')
    return user1, user_value



def main():
    user1, user_value = get_user_data()
    try:
        tuple1[user1] = user_value
        print(f'Wartość {tuple1[user1]} została zmieniona na {user_value}.')
    except TypeError:
        print(f'Nie można modyfikować krotki')


if __name__ == "__main__":
    main()