s = input()
for i in s:
    if i.isdigit():
        continue
    print(i,end='')
	
# 	OR
#	s = input()
#	print(s.translate({ord(i): None for i in '123456789'}))	