# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
# model (str)
# rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.
from datetime import date

def car_year(dict_cars):
  year = date.today().year
  sub = year - dict_cars['rocznik']
  if sub >= 25:
    print(f"Gratulacje! Twój samochód {dict_cars['marka']} może być zarejestrowany jako zabytek")
  else:
    print(f"Twój samochód {dict_cars['marka']} jest jeszcze zbyt młody.")

dict_cars = {
  "marka": "Toyota",
  "model": "Yaris",
  "rocznik": 2009,
}
print(dict_cars)

car_year(dict_cars)