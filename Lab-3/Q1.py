import numpy as n
a=n.random.randint(1,50,size=(3,4))
print("The array is :\n",a,"\n")
#median
med=n.median(a)
print("Median is",med)
mea=n.mean(a)
print("Mean is :",mea)
std=n.std(a)
print("Standard deviation is :",std)
sum=n.sum(a)
print("Sum is :",sum)
sumr=n.sum(a,axis=1)
print("Sum of each row is :",sumr)

f=a.reshape([2,6])
print("\n",f)
