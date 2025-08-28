num1= int(input("Enter number: "))
num2= int(input("Enter number: "))
try:
    if num1%num2==0:
        print("Divisible")
    else: 
        print("Not divisible")    
except Exception as err:
    print("Type:", type(err).__name__)
    print("Message: ", err)
