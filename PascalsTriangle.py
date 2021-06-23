from math import factorial

n = int(input())
s = int(input())
for k in range(n):
    x = []
    for i in range(k + 1):
        x.append(s * factorial(k) // factorial(i) // factorial(k - i))
    print(*x)
	
	