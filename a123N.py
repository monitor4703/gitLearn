ind = [1, 2, 3, 1]
print(ind.index(4))

def PrintMy(n,m,Arr,A,B):
    print(n,m)
    print(Arr)
    print(A)
    print(B)

NMlist = input()
NMlist = NMlist.split()
NMlist = list(map(int,NMlist))
n = NMlist[0]
m = NMlist[1]

Array = input()
Array = Array.split()
Array = list(map(int,Array))

A = input()
A = A.split()
A = list(map(int,A))

B = input()
B = B.split()
B = list(map(int,B))

Happy = 0
for i in range(0,len(Array)):
    if A.count(Array[i]) > 0:
        Happy += 1

for i in range(0,len(Array)):
    if B.count(Array[i]) > 0:
        Happy -= 1

print(Happy)
'''
A = set(A)
B = set(B)
Sym = A.symmetric_difference(B)
'''

#PrintMy(n,m,Array,A,B)




# Enter your code here. Read input from STDIN. Print output to STDOUT