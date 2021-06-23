import sys
import math
n = int(input())
shirt = 0
jeans = 0 
socks = 0 
sweater = 0
for i in range(n):
    item = input()
    if 'shirt' in item.lower():
        shirt += 1
    elif 'jeans' in item.lower():
        jeans += 2
    elif 'sock' in item.lower():
        socks += 0.5
    elif 'sweater' in item.lower():
        sweater +=3
print(min(shirt,jeans,math.floor(socks),sweater))