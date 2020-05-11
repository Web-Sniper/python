n = int(input("Enter an odd number: "))
if n%2==0 :
	print('Not a valid number...')
else:
	j=n//2
	for i in range(1,n+1,2):
		print(' '*j,'*'*i)
		j=j-1

