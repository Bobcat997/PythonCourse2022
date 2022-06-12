from BMI import calc_bmi, get_bmi_status

def open_advice(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        advice = f.read()

    return advice

def main():
    w = float(input("Podaj wagę [kg]"))
    h = float(input("Podaj wzrost [m]"))

    result = calc_bmi(h, w)
    status = get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(),'*************')
    print(advice)


main()