n = 0
a = 1
my_list = []
tab = []
while n < 10:
    for i in range(1,11):
        my_list.append(i*a)

    my_list = [my_list]
    tab.append(my_list)

    n += 1
    a += 1

    my_list.clear()

print(tab)
