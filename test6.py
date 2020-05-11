from itertools import groupby,repeat
a = input()
b= []
for i in groupby(a):
	b.append(i)
print(repeat('1',a))
print(b)