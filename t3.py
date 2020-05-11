n = int(input())
s = input()
s1 = set(s)
c = 0
for i in s1:
      print("s1",i)
      for j in s:
            if j==i:
                  c=c+1
                  print("s",j)
print(c)
