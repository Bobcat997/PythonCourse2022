# 4:Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron
books_title = input('Enter the title of the book')
author_name = input("Enter the author's name")
number_of_pages = input('Enter the number of pages')
book = books_title.replace(" " , "") + author_name.replace(" " , "") + number_of_pages

print(f'Czy {books_title.capitalize()}-->', books_title.replace(" " , "").isalpha())
print(f'Czy {author_name.capitalize()}-->', author_name.replace(" " , "").isalpha())
print(f'Czy {number_of_pages}-->', number_of_pages.isdigit())
print(book)
print(len(book))