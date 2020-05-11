n = int(input("Enter the number of row: "))
star = n*2-1
j=n-1
for i in range(1,star+1,2):
	print(' '*j,'*'*i)
	j=j-1
j = 0
for i in range(star,0,-2):
	print(' '*j,'*'*i)
	j=j+1