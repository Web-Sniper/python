t = int(input())
n = []
res = 0
for i in range(t):
    n1 = int(input())
    n.append(n1)
for i in n:
    if i%10==9:
        res = 1
        print(res)
    elif i%9==0:
        res = int(i/9)
        print(res)
    elif i<9:
          res = -1
          print(res)
    else:
        j = i
        while(j>9):
            t1 = 9
            t2 = j%t1
            t3 = (int(j/t1))-1
            j = j-t2+9
            t1 = t1+10
            
            if t2==0:
                break
            res = res+t3
        if t2==0:
            print(res)
        else:
            res = -1
            print(res)
