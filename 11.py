a1 = int(input("Enter angle1-"))
a2 = int(input("Enter angle2-"))
a3 = int(input("Enter angle3-"))


if a1 + a2 + a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    if a1 == 90 or a2 == 90 or a3 == 90:
        print("Right Triangle")
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")