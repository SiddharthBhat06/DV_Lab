import numpy as n
a=n.random.randint(1,100,size=(3,3))
b=n.random.randint(1,100,size=(3,3))
print("Matrix addition result :\n",a+b)
print("Matrix subtraction result :\n",a-b)
print("Matrix multiplication result(element wise) :\n",n.multiply(a,b))
print("Matrix multiplication result(dot product) :\n",n.dot(a,b))
print("Transpose result :\nof A :\n",a.T,"of B:\n",b.T)
print("Determinant of array a :\n",n.linalg.det(a))
print("Determinant of array b :\n",n.linalg.det(b))
print("inverse of array a :\n",n.linalg.inv(a))
print("inverse of array b :\n",n.linalg.inv(b))
