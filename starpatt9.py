n = int(input("Enter the number of row: "))
j = n-1
k = 1
l = 1
print(' '*(j+1),'*')
for i in range(1,n):
	j=j-1
	print(' '*j,'*',' '*k,'*')
	k=k+2
k = k-4
j = 1
for i in range(1,n-1):
	print(' '*j,'*',' '*k,'*')
	k=k-2
	j=j+1
j=n-1
print(' '*(j+1),'*')