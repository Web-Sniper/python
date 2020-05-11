a = int(input("Enter the number : "))
fact = 1
if a==0 or a==1:
	print("Factorial of ",a," = 1")
else :
	for i in range(1,a+1):
		fact = fact * i
	print("Factorial of ",a," = ",fact)