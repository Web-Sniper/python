from itertools import combinations,permutations
a,b = input().split()
b=int(b)
res = set()
res1 = set()
t = permutations(a,b)
t1 = combinations(a,b)
for i in t:
    res.add(''.join(i))
for i in t1:
	res1.add(''.join(i))
#res.sort()
a = list(a)
a.sort()
res = list(res.difference(res.difference(res1)))
res.sort()
for i in a:
    print(i)

for i in res:
    print(i)