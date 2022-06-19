from io import UnsupportedOperation

try:
    with open('test.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

except IOError:
    print('Wystąpił błąd podczas odczytu pliku - brak dostępu do pliku.')

try:
    File1 = open('test1.txt', 'w')
    contents2 = File1.read()
    File1.close()

except UnsupportedOperation:
    print('Wystąpił błąd podczas odczytu pliku - plik nie jest do odczytu.')

try:
    with open("test2.txt", "x") as fh:
        fh.write("Dane testowe")

except FileExistsError:
    print('Wystąpił błąd podczas tworzenia pliku - plik już istnieje.')