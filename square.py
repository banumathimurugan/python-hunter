n=int(input())
s=0
if(n>1 and n<10000000000000000000000):
  while(n!=0):
    r=n%10
    s+=r*r
    n//=10
print(s)
