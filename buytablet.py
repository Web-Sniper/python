t = int(input())
l = []
res = []
for i in range(0,t):
	n,b = input().split()
	n = int(n)
	b = int(b)
	for i in range(1,n+1):
		w,h,p= input().split()
		w = int(w)
		h = int(h)
		p = int(p)
		e=[]
		e.append(w)
		e.append(h)
		e.append(p)
		l.append(e)
	sortlist = []
	for i in range(0,len(l)):
		if l[i][2]<=b:
			sortlist.append(l[i])
	if len(sortlist)==0:
		e ='no tablet'
		res.append(e)
	else:
		dim = []
		for i in range(0,len(sortlist)):
			d = sortlist[i][0]*sortlist[i][1]
			dim.append(d)
		res.append(max(dim))
	sortlist.clear()
print(sortlist)
for i in res:
	print(i)


