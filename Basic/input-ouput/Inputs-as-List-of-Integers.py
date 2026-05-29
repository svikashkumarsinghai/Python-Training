""" Explanation: This code defines a function get_list() that reads a line of input, 
splits it into components, converts each component to an integer, 
and returns the result as a list of integers. The function uses sys.stdin.readline() 
to read the input and map(int, ...) to convert the split strings into integers. Finally, 
it calls get_list() and stores the result in the variable Arr. """

import sys
def get_list(): 
    return list(map(int, sys.stdin.readline().strip().split()))
Arr = get_list()
print("List of integers:", Arr)

"""Results in a list of integers from the input
22, 33, 44, 55
output: List of integers: [22, 33, 44, 55]"""

# for string input
import sys
def get_string(): 
    return sys.stdin.readline().strip()
string = get_string()

print("String input:", string)

"""Results in a string from the input
Hello World
output: String input: Hello World