text = "Abrakadabra"
magic = "Hokus pokus"
letter = "Welcome to Hogwart"


def find_longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def show(text):
    print('*' * 50)
    print(text.center(50))
    print('*' * 50)



