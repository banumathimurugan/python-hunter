n=int(input())
arr=[int(x) for x in input().split()]
a=0
for i in arr:
  a=0
  for j in arr:
    if i==j:
      a+=1
  if a==1:
    print(i)
