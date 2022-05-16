usage_fuel = float(input('Spalanie paliwa(l)'))
distance = float(input('Podaj dystans wyprawy(km)'))
price_of_fuel = float(input('Cena paliwa(zł)'))

cost = price_of_fuel /100 * distance * usage_fuel
print('Cena = ', round(cost,2), 'PLN')