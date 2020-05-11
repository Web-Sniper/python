import math
def chess(s,d):
      while True:
            if s[0]==d[0] and s[1]==d[1]:
                  break
            else:
                  t = []
                  t2 = []
                  t.append([s[0]-1,s[1]-1])
                  t.append([s[0]-1,s[1]+1])
                  t.append([s[0]+1,s[1]-1])
                  t.append([s[0]+1,s[1]+1])
                  t.append([s[0],s[1]-1])
                  t.append([s[0],s[1]+1])
                  t.append([s[0]-1,s[1]])
                  t.append([s[0]+1,s[1]])
                  for j in t:
                        temp = 0
                        l = 0
                        for k in j:
                              temp = temp+(k-d[l])**2
                              l = l+1
                        t2.append(math.sqrt(temp))
                  idx = t2.index(min(t2))
                  s = t[idx]
                  print(s)
                  
                              

s = [1,8]
d = [8,1]
chess(s,d)
