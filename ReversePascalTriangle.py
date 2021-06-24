#Given a list of integers they add consecutive pairs of integers row by row until
#the triangle is reduced to one final ineger sum.
# example 1 1 1 1       1 1 1 1  
#                  ->    2 2 2 
#                         4 4
#                          8 
#  

input()
k = list(map(int, input().split()))
while len(k) > 1:
    k = [k[i] + k[i+1] for i in range(len(k)-1)]

print(k[0])