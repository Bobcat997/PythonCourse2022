numbers = '325354756'
mixed = 'q34324ffagtr43'

print(f'Ciąg {numbers} zawiera same cyfry ->', numbers.isdigit())
print(f'Ciąg {mixed} zawiera same cyfry ->', mixed.isdigit())

# ----

txt = 'mata'
centered_txt = txt.center(10, '*')
print(centered_txt)

# ---
url = 'www.example.com'
new_url = url.lstrip('w.')
print(new_url)


dna = 'AAATTTGGCCAAAAAA'
cleaned_dna = dna.rstrip('A')
print(cleaned_dna)
# ---

password = 'AdminAdminTakNieRobHasla'

includes_at_least_1_upper = password.isalpha() and (not password.islower() and not password.isupper() )

print(includes_at_least_1_upper)

# ---
fruit = 'banana'
counter = fruit.count('na')
print(counter)


quote = '„Honesty is the first chapter in the book of wisdom.”'
# Policz wszystkie znaki w napisie
print(len(quote))
# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-9:-2])
# Wyświetl tylko pierwszą połowę tekstu
mid_index = len(quote)//2
print(quote[:mid_index + 1])
# Wyświetl tylko kropkę
print(quote[-2])
# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[::2])
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[mid_index::3])
# Wyświetl cały cytat odwrotnie
print(quote[::-1])
# Zamień wisdom na słowo friendship
print(quote.replace('wisdom', 'friendship'))
