# 5▹ Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def remove_extras(text):
    for char in '!,.()':
        text = text.replace(char, '')

    text = text.replace('\n', ' ')
    return text


def find_longest_word(text):
    longest = ''
    for word in text:
        if len(word) > len(longest):
            longest = word
    return longest


def main():
    with open('examples/tekst.txt', encoding='utf-8') as fopen:
        content = fopen.read()

    content = remove_extras(content)
    content = content.split()
    longest_word = find_longest_word(content)
    print(longest_word)


main()
