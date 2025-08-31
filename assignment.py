try:
    age=int(input("Enter your age: "))
    if age%2==0:
        print("Number is even.")   
    else:
        print("Number is odd.")    
except ValueError as ex:
    print("Exception: ", ex)
             