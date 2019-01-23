N1=10
N2=14
N3=15
if (N1 >= N2) and (N1 >= N3):
  largest = N1
elif (N2 >= N1) and (N2 >= N3):
  largest =N2
else:
  largest = N3
print("The largest number between",N1,",","N2","and",N3,"is",largest)
