# This is a simple Python program to demonstrate input and output.
Name =  "Vikash Kumar!"
age = 25
City = "Bangalore"
print("Name of student is",Name,"and age is",age,"and city is",City)

# Taking input from user and performing addition
x,y = int(input("Enter first number: ")),int(input("Enter second number: "))
print("The sum of",x,"and",y,"is",x+y)

x,y = input("Enter the numbers  ").split()
print(x,y)

#Taking Different types of User Input
i = int(input("Enter an integer: "))
f = float(input("Enter a floating-point number: "))
print("You entered the integer:", i,f)