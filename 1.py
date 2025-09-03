a=int(input("enter your 1st number."))
b=int(input("enter your 2nd number."))
c=int(input("enter your 3rd number."))
if ((a>b) and(b>c)):
    print( c,"is minimum number")
elif(b>c) :
    print(a, "is minimum number")
elif(c>a) :
    print(b, "is minimum number")
else:
    print("number are same pls enter coreect numbers")  