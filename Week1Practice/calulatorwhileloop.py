#Example of calculate through while loop. no need to indicate divide by zero but using Zerodivision error instead
#Use if XXX in [] not (), if elif, print(f"Result: {result}\n")
#Use float cuz result can be in decimal for division
#Becareful, True should be the big T
#Becareful, after print(f"Result: {result}\n"), next elif should be inline with main command.
#Dont forget calculator() at the end 

def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Error: number cant be divided by Zero"
    
def calculator():
    print("Simple calculation")
    print("------------------")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

while True:
    choice = (input("Enter choice (1/2/3/4)"))

    if choice in ["1","2","3","4"]:
        num1=float(input("Enter first number"))
        num2=float(input("Enter second number"))

        if choice == "1":
            result = add(num1,num2)
        elif choice == "2":
            result = substract(num1,num2)
        elif choice == "3":
            result = multiply(num1,num2)
        elif choice == "4":
            result = divide(num1,num2)
        print(f"Result: {result}\n")
    
    elif choice == "5":
            break
    else:
        print("Number is invalid, please try again")

calculator()
