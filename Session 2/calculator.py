def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "ERROR: CANNOT DIVIDE BY ZERO"

def surplus(num1, num2):
    return num1 % num2
    
def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Devide")
    print("5. Surplus")

    choice = input()

    if choice == "1":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(add(num1,num2))
    
    if choice == "2":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(substract(num1, num2))
    
    if choice == "3":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(multiply(num1, num2))

    if choice == "4":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(divide(num1, num2))

    if choice == "5":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(surplus(num1, num2))  

calculator()
