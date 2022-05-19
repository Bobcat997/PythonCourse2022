#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.


w = float(input('Dodaj wage(kg)-->'))
h = float(input('Dodaj wzrost(m)-->'))

BMI = w / (h**2)

if BMI < 18.49:
    print("Niedowaga", round(BMI, 2))
elif BMI < 25:
    print("waga normalna", round(BMI, 2))
elif BMI > 25 and BMI < 30:
    print("nadwaga", round(BMI, 2))
elif BMI > 30:
    print("otyłość", round(BMI, 2))
