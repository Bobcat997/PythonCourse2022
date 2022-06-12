import os

filename = input('Podaj nazwe pliku do odczytu ->')
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('Nie ma takiego pliku')