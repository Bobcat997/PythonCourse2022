def find_multiple(a, n):
    multiples = []
    for i in range (1, n):
        if i * a < n:
            multiples.append(i * a)

    return multiples


def main():
    a = int(input('a -> '))
    b = int(input('b -> '))
    n = int(input('n -> '))
    multiples = find_multiple(a, n) + find_multiple(b, n)
    sum_of_multiples = 0
    for v in multiples:
        sum_of_multiples += v
    print(sum_of_multiples)

if __name__ == '__main__':
     main()
