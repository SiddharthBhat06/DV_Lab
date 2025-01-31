wcwin={2003:'Australia',2007:'Australia',2011:'India',2015:'Australia',2019:'England',2023:'Australia'}
l=[]
max=0
for i in wcwin.values():
    co=0
    for j in wcwin.values():
        if i==j:
            co+=1
    if co>max:
        best=i
        max=co
print(best,"Is the best performing country with",max,"wins")
for i in wcwin.values():
    if i not in l:
        l.append(i)
print(l)
    
