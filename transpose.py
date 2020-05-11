def transpose(a,l):
      res = []
      for i in range(l):
            temp = []
            for j in a:
                  if i>=len(j):
                        temp.append(" ")
                  else:
                        temp.append(j[i])
            temp = "".join(x for x in temp)
            res.append(temp)
      return res
                  

a = ['Atul','Yellow','Kumar', 'h']
length = len(a[0])
for i in a:
      if len(i)>length:
            length = len(i)
t = transpose(a,length)
print(t)
