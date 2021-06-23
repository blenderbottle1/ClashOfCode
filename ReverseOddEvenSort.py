import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = set([int(i) for i in input().split()])
odd = []
even = []
for i in s:
    if i% 2 != 0:
        odd.append(i)
    else:
        even.append(i)
odd.sort()
even.sort()
print(*(odd+even[::-1]))
