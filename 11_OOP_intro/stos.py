class Stack:
    def __init__(self, lifo=[]):
        self.lifo = lifo


    def show(self):
        print('Stack -->', self.lifo)


    def push(self, item):
        self.lifo.append(item)

    def get(self):
        return self.lifo.pop(-1)


def main():
    q = Stack([3, 2, 6])
    q.push('bobek')
    q.show()
    x = q.get()
    print('wyjęto -->', x)
    q.show()


if __name__ == '__main__':
    main()