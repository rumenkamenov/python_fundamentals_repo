degrees = int(input())
text = input()

Outfit = None
Shoes = None

if text == "Morning":
    if degrees <= 10 and degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif degrees > 18 and degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
if text == "Afternoon" and  degrees <= 10 and degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    if  degrees > 18 and degrees <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif degrees >= 25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'

elif text == "Evening" and  degrees <= 10 and degrees <= 18:
    Outfit = "Shirt"
    Shoes = "Moccasins"
elif degrees > 18 and  degrees <= 24:
    Outfit = 'Shirt'
    Shoes = 'Moccasins'
elif degrees >= 25:
    Outfit = 'Shirt'
    Shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")