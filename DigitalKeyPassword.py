'''
You have a digital lock which can be opened typing a series of K digits from 0 - 9.
You can also type any digits before or after any member of the K digits,
the lock will open after typing each digit of K at least once in order.

Print yes or no whether the given T digits opens the lock.

Input
12345
3
712304256
54321234
67890

Output
yes
no
no
'''

key = input()
n = int(input())
for i in range(n):
    line = input()

    keyI = 0
    #read each char in line
    for c in line:
        #check if current char is in key based on index
        if c == key[keyI]:
            #increment key 
            keyI += 1
            #if length of keyI is greater than the key, we have obtained our password
            if keyI > len(key)-1:
                break
            
            

    if keyI > len(key)-1:
        print("yes")
    else:
        print("no")
 