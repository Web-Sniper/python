T = int(input())
N,A,B,K = input().split()
N = int(N)
A = int(A)
B = int(B)
K = int(K)
c = 0
for i in range (0,T) :
    for i in range(1,N+1):
        if i%A == 0 and i%B!=0:
            c = c+1
        elif i%B == 0 and i%A!=0:
            c = c+1
if c==K:
    print("win")
else :
    print("lose")
