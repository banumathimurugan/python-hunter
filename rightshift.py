def rotate(1st,y):
  return[1st[-x:] + 1st[:-y]]
l=list(map(int,input().split(' ')))
p=int(inout())
print(''.join(str(y) for y in rotate(1,p)))
