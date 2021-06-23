_hex = input()[2:]
x = []
for i in range(4):
    x += [int(_hex[i*2:i*2+2],16)]
print(".".join(str(i)for i in x))
