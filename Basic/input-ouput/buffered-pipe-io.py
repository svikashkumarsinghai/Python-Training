"""When inputs/outputs are very large, even sys.stdin may not be enough. In such cases, we can use a buffered pipe (io.BytesIO) to further speed up I/O. 
This is more advanced and usually required only for problems with huge input sizes (2MB+ files).
"""

import atexit, io, sys

# A buffer for output
buffer = io.BytesIO()
sys.stdout = buffer

# Print via buffer
@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())

#####################################
# Example program
n = int(input())
arr = [int(x) for x in input().split()]
summation = sum(arr)
print(summation)

# Explanation: Output is written into an in-memory buffer instead of directly printing. At program exit, atexit.register writes all data at once. This reduces the overhead of multiple print() calls.