def prime(n):
      res = []
      i = 2
      while(n!=1):
            if n%i==0:
                  res.append(i)
                  n = n/i
            else:
                  i = i+1
      return res

n = int(input("Enter the number>1: "))
p = prime(n)
if n==1:
      print("You entered 1, Try again!")
else:
      print("Prime Factors of",n,": ",end=" ")
      for i in range(len(p)):
            print(p[i],end=" ")
            if i!=len(p)-1:
                  print(end="* ")
      

