n = int(input("Enter the odd number of star: "))
l = n//2
r = n//2
j = 1
print('*'*n)
for i in range(1,l+1):
	print('*'*l+' '*j+'*'*r)
	l = l-1
	r= r-1
	j = j+2
l = 2
r = 2
j=n-4

for i in range(1,n//2):
	print('*'*l+' '*j+'*'*r)
	l = l+1
	r = r+1
	j=j-2
print('*'*n)


