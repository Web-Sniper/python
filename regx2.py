import sys,re
for i in sys.stdin:
   x = re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})',i,re.I)
   for j in x:
       print(j)


