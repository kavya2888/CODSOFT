# Simple Calculator with basic arithmetic operations

# Function to display operator menu
def display_menu() :
    print("Enter 1 : To Add")
    print("Enter 2 : To Subtract")
    print("Enter 3 : To Multiply")
    print("Enter 4 : To Divide")

# Function to add two numbers
def add(num1,num2) :
    print(num1,"+",num2,"=",num1 + num2)

# Function to subtract two numbers
def sub(num1,num2) :
    print(num1,"-",num2,"=",num1 - num2)

# Function to multiply two numbers
def mul(num1,num2) :
    print(num1,"*",num2,"=",num1 * num2)

# Function to divide two numbers
def div(num1,num2) :
    if num2 == 0 :
        print("Error. Cannot divide by zero.")
    else :
        print(num1,"/",num2,"=",num1 / num2)
   
display_menu()

number1 = int(input("Enter the first number :  "))
number2 = int(input("Enter the second number : "))

choice = int(input("Enter your choice number(1/2/3/4) :"))

print("Result :")

if choice == 1 :
    add(number1,number2)
elif choice == 2 :
    sub(number1,number2)
elif choice == 3 :
    mul(number1,number2)
elif choice == 4 :
    div(number1,number2)
else :
    print("Invalid Choice.Try Again!")



       
