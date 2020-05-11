r,c= input().split()
r = int(r)
c = int(c)
m = 1
l = int((c-3)/2)
r = l
n = int(r//2)
for i in range(0,n):
    print('-'*l+'.|.'*m+'-'*r)
    if l==3 and r==3:
    	break
    m = m+2
    l = l-3
    r = r-3
    
w = int((c-7)/2)
l = 3
r = 3
m = int((c-6)/3)
print('-'*w+'Welcome'+'-'*w)
for i in range(0,n):
    print('-'*l+'.|.'*m+'-'*r)
    if m==1:
    	break
    r= r+3
    l=l+3
    m=m-2
    

