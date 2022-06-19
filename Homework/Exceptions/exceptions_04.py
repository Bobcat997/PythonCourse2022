def data_collect():
    user_input = input(f'Podaj liczby całkowite, oddzielając je przecinkami -->')
    user_input = user_input.split(",")
    try:
        for i in range(0, len(user_input)):
            user_input[i] = int(user_input[i])
    except ValueError:
        with open('error_list.txt', 'w', encoding='UTF-8') as f:
            f.write(f'Wystąpił błąd "ValueError"')
            error()
    except TypeError:
        with open('error_list.txt', 'w', encoding='UTF-8') as f:
            f.write(f'Wystąpił błąd "TypeError"')
            error()
    return user_input


def average_val():
    user_numbers = data_collect()
    val_sum = 0
    for i in range(0, len(user_numbers)):
        val_sum += user_numbers[i]
        average = val_sum / len(user_numbers)
    return average


def error():
    print(f'Podałeś niepoprawne dane')


def main():
    print(f'Średnia arytmetyczna z podanych liczby wynosi: {average_val()}')


main()


