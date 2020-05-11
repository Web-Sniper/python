n = int(input("Enter the odd number: "))
if n%2==0:
	print("Not a valid number")
else:
	j = 0
	for i in range(n,0,-2):
		print(' '*j,'*'*i)
		j=j+1
	j=n//2-1
	for i in range(3,n+1,2):
		print(' '*j,'*'*i)
		j=j-1