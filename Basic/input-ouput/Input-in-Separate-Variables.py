#Taking User Input in Separate Variables

"""Explanation: get_ints() uses map(int, split()) to convert input into integers. 
The values are directly assigned to variables in one line."""

import sys
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())
a, b, c, d = get_ints()
print("a =", a, "b =", b, "c =", c, "d =", d)

"""Example Input:5 7 19 20
Example Output:a = 5 b = 7 c = 19 d = 20