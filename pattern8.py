n=int(input("enter number"))

for i in range(n):         
    for j in range(n):       
        if j < n - i - 1:    
            print("_", end="")
        else:                
            print("*", end="")
    print()