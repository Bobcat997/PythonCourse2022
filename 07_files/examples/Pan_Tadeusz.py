filename = 'tekst.txt'

with open(filename, 'r', encoding='UTF-8') as f:
  content = f.read()
  print(content)