from BMI import calc_bmi, get_bmi_status

def open_advice(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        advice = f.read()

    return advice

def get_value(message, min_max):
    while True:
        try:
            value = float(input(message))
            minium, maxium = min_max
            if value in range(minium, maxium):
                pass
            else:
                raise ValueError(f'Wartość {value} poza zakresem {min_max}')
        except (TypeError, ValueError):
            print('Wartość jest nie prawidłowa, spróbuj jeszcze raz')
        else:
            return value



def main():
    w = get_value('Podaj wagę [kg]', (20, 200))
    h = get_value("Podaj wzrost [cm]", (140, 250))/100

    result = calc_bmi(h, w)
    status = get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(),'*************')
    print(advice)


main()