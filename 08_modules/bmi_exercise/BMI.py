def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga_normalna"
    elif bmi < 30:
        return "nadwaga",
    else:
        return "otylosc"
