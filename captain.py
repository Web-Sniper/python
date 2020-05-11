k = int(input())
room = list(map(int,input().split()))
r1 = set(room)
c = 0
for i in r1:
    if room.count(i)==1:
        c=i
        break
print(c)
