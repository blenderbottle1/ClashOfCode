a = int(input())
b = int(input())

count = 0
for i in range(a,b+1):
    if i&3==0:
        if i % 100 == 0:
            if i % 400 == 0:
                count+=1
                continue
            else:
                continue
        count+=1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)
