#x= int(input("Enter a number: "))

arr = [int(x) for x in input("Enter the numbers: ").split()]
sum = 0
print(arr)  # This will print the list of numbers entered by the user
for i in arr:
    sum += i    
print("The sum of the numbers is:", sum)
#-----------------------------------------------------------------------
# another way to calculate the sum using built-in function
n = int(input()) #
arr = [int(x) for x in input().split()]
summation = 0
for x in arr:
    summation += x
print(summation)

/*"""  Explanation:

first line n = int(input()) takes the number of elements.
second line reads the elements as space-separated integers.
loop calculates the sum and finally, print() displays the result. """*/