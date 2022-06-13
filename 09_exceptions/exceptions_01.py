# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.


numbers = [13, 'hello', 2.45, True, None, 0,]

for i in numbers:
    try:
        result = 10/i
        print(result)
    except (TypeError, ZeroDivisionError):
        print(f'10/{i} Nie można wykonać')





