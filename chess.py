def chess(s,d):
      d1 = s[0]-d[0]
      d2 = s[1]-d[1]
      print("Steps are: ")
      if d1/abs(d1)==-1:
            for i in range(abs(d1)):
                  s[0]=s[0]+1
                  print(s[0],s[1])

      else:
            for i in range(abs(d1)):
                  s[0]=s[0]-1
                  print(s[0],s[1])
      if d2/abs(d2)==-1:
            for i in range(abs(d2)):
                  s[1]=s[1]+1
                  print(s[0],s[1])
      else:
            for i in range(abs(d2)):
                  s[1]=s[1]-1
                  print(s[0],s[1])          

s = [1,8]
d = [8,1]
chess(s,d)
print("Arrived at destination.....")
