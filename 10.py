a=int(input("enter your 1st number."))
b=int(input("enter your 2nd number."))
c=int(input("enter your 3rd number."))
if ((a>b) and(a>c)):
    print( a,"is maximum number")
elif((b>c)  and (b>a)):
    print(b, "is maximum number")
elif((c>a) and (c>b)):
    print(c, "is maximum number")
else:
    print("invalid input")
 