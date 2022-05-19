txt = "Pythaaa"
if len(txt) > 5:
    if 'a' in txt:
        print(txt.replace('a', 'z'))
    print("Jest dłuższy niż 5 znaków")
else:
    print("Ma mniej niz 5 znaków")