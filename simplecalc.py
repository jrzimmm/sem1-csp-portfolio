#Simple Calculator

#Init
import math
#Functions

#Adds two numbers together and gives the sum
def add(num1,num2):
    result = num1 + num2
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Subtracts two numbers together and gives the difference
def subtract(num1,num2):
    result = num1 - num2
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Multiplies two numbers together and gives the product
def mult(num1,num2):
    result = num1 * num2
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Divides two numbers and gives the result, with error handling for 0/0
def divide(num1,num2):
    if num2 == 0:
        print("CANNOT DIVIDE BY ZERO!")
    else:
        result = num1 / num2
        print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Raises the first number entered to the second number's power (num1^num2)
def exponent(num1,num2):
    result = num1 ** num2
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Roots the first number entered to the second number's power (num2^root(num1)))
def root(num1,num2):
    if num1 > 0:
        result = num1 ** (1/num2)
        print("Calculation (IMAGINARY NUMBERS) " + str(calcCount) + " EQUALS: " + str(result))
    else:
        result = num1 ** (1/num2)
        print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Gives sin function from an entered degree value
def functionSin(num1):
    result = math.sin(num1)
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Gives cos function from an entered degree value
def functionCos(num1):
    result = math.cos(num1)
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Gives tangent function from an entered degree value
def functionTan(num1):
    result = math.tan(num1)
    print("Calculation " + str(calcCount) + " EQUALS: " + str(result))

#Main
operation = 0
calcCount = 0
#Introduction/menu
print("Welcome Preschooler to Simple Calc")
print("Enter a calculation: ")
print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Close Calculator

OR TRY AN ADVANCED CALCULATION
6. Exponential
7. Root
8. Sine Function
8. Cosine Function
8. Tangent Function
""")

#IMPUT VALUES WHEN ONE OF THE CALCULATION TYPES IS SELECTED

while operation != 5:
    operation = int(input("(1-5) Operation: "))
    if operation == 1:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number!"))
        calcCount = calcCount + 1
        add(int1, int2)

    if operation == 2:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number!"))
        calcCount = calcCount + 1
        subtract(int1, int2)


    if operation == 3:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number!"))
        calcCount = calcCount + 1
        mult(int1, int2)

    if operation == 4:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number!"))
        calcCount = calcCount + 1
        divide(int1, int2)

    if operation == 6:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number!"))
        calcCount = calcCount + 1
        exponent(int1, int2)

    if operation == 7:
        int1 = int(input("Enter your first number!"))
        int2 = int(input("Enter your second number (THIS IS WHAT YOU ARE ROOTING BY!)"))
        calcCount = calcCount + 1
        root(int1, int2)

    if operation == 8:
        int1 = int(input("Enter your first number!"))
        calcCount = calcCount + 1
        functionSin(int1)

    if operation == 9:
        int1 = int(input("Enter your first number!"))
        calcCount = calcCount + 1
        functionCos(int1)

    if operation == 10:
        int1 = int(input("Enter your first number!"))
        calcCount = calcCount + 1
        functionTan(int1)
