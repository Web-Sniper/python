def vword(s):
	j=1
	kp=0
	while(j!=len(s)+1):
		for i in range(0,len(s)+1-j):
			sub=s[i:i+j]
			if sub[0] in vowels:
				kp=kp+1
		j=j+1
	return kp
def cword(s):
	j=1
	sp=0
	while(j!=len(s)+1-j):
		for i in range(0,len(s)+1-j):
			sub=s[i:i+j]
			if sub[:1] not in vowels:
				sp = sp+1
		j=j+1
	return sp
vowels = 'AEIOU'
s = input()
kp=vword(s)
sp=cword(s)
if kp>sp:
	print('Kelvin ',kp)
elif kp<sp:
	print('Stuart ',sp)
else:
	print('Draw')