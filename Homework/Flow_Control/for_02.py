ingredients = ['spinach', 'pasta', 'oil', 'cream', 'grated Parmesan cheese', 'onion', 'garlic cloves']
step_1 = "Makaron ugotować al dente w osolonej wodzie. Szpinak opłukać i odcedzić."
step_2 = "Na patelni na oliwie i maśle zeszklić pokrojoną w kosteczkę cebulę (ok. 5 - 7 minut). Doprawić solą, dodać przeciśnięty przez praskę czosnek i smażyć jeszcze przez ok. 2 minuty."
step_3 = "Dodać szpinak i mieszając podgrzewać przez ok. 1 minutę aż zwiędnie."
step_4 = "Wlać śmietankę, doprawić świeżo zmielonym pieprzem i solą, całość zagotować. Dodać odcedzony makaron i wymieszać."
step_5 = "Połączyć z 1/3 ilości sera, resztę wykorzystać do posypania makaronu."

for index in ingredients:
    print('-', index)
    if index == 'pasta':
        print(step_1)
    if index == 'oil':
        print(step_2)
    if index == 'spinach':
        print(step_3)
    if index == 'cream':
        print(step_4)
    if index == 'grated Parmesan cheese':
        print(step_5)