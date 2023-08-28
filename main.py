def cm_to_in(cm):
    inches = cm / 2.54
    return inches
def m_to_ft(meters):
    ft = meters * 3.28084
    return ft
def km_to_mi(km):
    mi = km * 0.621371
    return mi
def kg_to_pound(kg):
    pounds = kgs * 2.20462
    return pounds
def grams_to_oz(g):
    oz = grams * 0.03527396
    return oz
def celsius_to_f(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
def celsius_to_k(celsius):
    kelvin = celsius + 273.15
    return kelvin
def ml_to_cups(ml):
    cups = mls / 237
    return cups
def liters_to_gallons(liters):
    gallons = liters * 0.264172
    return gallons


print ("Unit Converter")
print("Categories: ")

print("1 - Length")
print("2 - Mass")
print("3 - Temperature")
print("4 - Volume")

cat = int(input("Select one option: "));

print("Available convertions: ")

if cat == 1:
    print("1 - Centimeters to inches")
    print("2 - Meters to feet")
    print("3 - Kilometers to miles")
    sel = int(input("Select the desired operation: "))

    if sel == 1:
        cm = float(input("Centimeters: "))
        print("The result is", cm_to_in(cm), "inches.")
    elif sel == 2:
        meters = float(input("Meters: "))
        print("The result is", m_to_ft(meters), "feet.")
    elif sel == 3:
        km = float(input("Kilometers: "))
        print("The result is", km_to_mi(km), "miles.")
    else:
        print("Invalid option!")

elif cat == 2:
    print("1 - Kilograms to pounds")
    print("2 - Grams to ounces")
    sel = input("Select the desired operation: ")

    if sel == 1:
        kgs = float(input("Kilograms: "))
        print("The result is", kg_to_pound(kgs), "pounds.")
    elif sel == 2:
        grams = float(input("Grams: "))
        print("The result is", grams_to_oz(grams), "ounnces.")
    else:
        print("Invalid option!")

elif cat == 3:
    print("1 - Celsius to Fahrenheit")
    print("2 - Celsius to Kelvin")
    sel = input("Select the desired operation: ")

    if sel == 1:
        celsius = float(input("Degrees in C°: "))
        print("The result is", celsius_to_f(celsius), "Fahrenheit.")
    elif sel == 2:
        celsius = float(input("Degrees in C°: "))
        print("The result is", celsius_to_k(celsius), "Kelvin.")
    else:
        print("Invalid option!")

elif cat == 4:
    print("1 - Mililiters to cups")
    print("2 - Liters to gallons")
    sel = input("Select the desired operation: ")

    if sel == 1:
        mls = float(input("Mililiters: "))
        print("The result is", ml_to_cups(mls), "cups.")
    elif sel == 2:
        liters = float(input("Liters: "))
        print("The result is", liters_to_gallons(liters), "gallons.")
    else:
        print("Invalid option!")
else:
    print("Invalid option!")