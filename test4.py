def minion_game(string):
    s = string
    ls = list()
    l1 = set()
    l2 = set()
    c1 = 0
    c2 = 0
    for i in range(0,len(s)):
        for j in range(len(s),0,-1):
        	if s[i:j] !="":
        		ls.append(s[i:j])
    for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                l1.add(i)
            else :
                l2.add(i)
    for i in l1:
        for j in ls:
            if j[0:1]==i:
                c1 = c1+1
    for i in l2:
        for j in ls:
            if j[0:1]==i:
                c2 = c2+1
    if c2>c1:
        print('Stuart',c2)
    elif c2<c1:
        print('Kevin',c1)
    else:
    	print('Draw')
    print(ls)
if __name__ == '__main__':
    s = input()
    minion_game(s)