# f = open('test1.txt')
# print(f.readlines())
# f.close()

with open('test1.txt') as f:
    content = f.readlines()

print(content)

for line in content:
    print(line)

with open('pan_tadeusz.txt', 'w') as f:
    f.write('Pan Tadeusz')