import random

def hot_cold(num,random_number1,random_number2,number_of_attempts):
    while number_of_attempts < 7:
        user_choice = int(input("Wprowadź liczbę "))
        if user_choice >= random_number1 and user_choice <= random_number2:
            print("Ciepło")
            number_of_attempts = 1 + number_of_attempts
        else:
            print("Zimno")
            number_of_attempts = 1 + number_of_attempts
        if user_choice == num:
            break
    if number_of_attempts > 6:
        print(f"Niestety moją liczbą była: {num}")
    else:
        print(f"Brawo, Moją liczbą była {num}")

def main():
    num = int(random.randrange(1, 100))
    number_of_attempts = 0
    random_number1 = num - 10
    random_number2 = num + 10
    hot_cold(num,random_number1,random_number2,number_of_attempts)
main()