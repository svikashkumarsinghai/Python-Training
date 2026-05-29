""" stdin.readline() reads input as raw text much faster.
stdout.write() avoids extra formatting overhead of print().
 """

from sys import stdin, stdout
def main():
    n = int(stdin.readline())  # Read the number of elements
    arr = [int(x) for x in stdin.readline().split()]
    summation = sum(arr)  # Calculate the sum using built-in function
    stdout.write(str(summation) + '\n')  # Write the result to standard output
if __name__ == "__main__":
    main()

