#raguljerish 
n,k=map (int,input("Enter limit number:").split ())
s=n
count=0
while n>0:
     n=n//10
     count=count+1
while s<=k:
     a=0
     for i in range (count):
       h=str(s)
       a=a+int(h[i])**count
     if s==a:
          print(s)
     s=s+1
