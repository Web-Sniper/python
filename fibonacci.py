a = int(input("Enter the range of fibonacci : "))
i = 0
j = 1
k = 0
if a==1:
	print("0")
elif a==2:
	print(i)
	print(j)
else : 
	print(i)
	while k<a:
		print(j)
		k = i+j
		i = j
		j = k
		

