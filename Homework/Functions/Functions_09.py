# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.

# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.

# ponownie wyświetl zmieniony słownik

# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

from datetime import date

def able_to_register(dict_cars):
  year = date.today().year
  sub = year - dict_cars['rocznik']
  if sub >= 25 and dict_cars['czy_orginalny']:
    print(f"Gratulacje! Twój samochód {dict_cars['marka']} może być zarejestrowany jako zabytek")
  else:
    print(f"Twój samochód {dict_cars['marka']} nie moze zostac zarejestrowany jako zabytek")

dict_cars = {
  "marka": "Toyota",
  "model": "Yaris",
  "rocznik": 1985,
  "czy_orginalny": True,
}
print(dict_cars)

able_to_register(dict_cars)
