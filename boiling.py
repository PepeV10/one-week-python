unit = input("What unit are you using? ").lower()
temp = int(input("What temperature is the water? "))

if unit == "f":
    if temp == 212:
        print("Water is Boiling!")
    else:
        print("Water is not boiling. Must hit 212F")
elif unit == "c":
    if temp == 100:
        print("Water is Boiling!")
    else:
        print("Water is not Boiling. Must hit 100C")
elif unit == "k":
    if temp == 373:
        print("Water is Boiling!")
    else:
        print("Water is not Boiling. Must hit 373K")
else:
    print("I don't know those units!")

# f - 212
# c - 100
# k - 373
