
def find_nwd(a, b):
    while True:
        rest = a % b

        if rest == 0:
            nwd = b
            return nwd
        else:
            a = b
            b = rest


a = int(input("a -> "))
b = int(input('b -> '))

nwd = find_nwd(a, b)
print(f'greatest common divisor {a} i {b} this {nwd}')