def circle_field(radius):
    return 3.14*radius**2


#--
radius = float(input("Podaj promień koła"))
field =circle_field(radius)
print('Pole koła to:', field)