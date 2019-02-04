#sum 101.py
#ragul jerish
n,k=map(str,input("enter a string & a number:").split())
s=len(n)
i=int(k)
while i>0:
	print(n[s-1],end="")
	i-=1
