try:
    dic1={}
    a=input("Enter string :")
    for i in a:
        co=0
        for j in a:
            if i==j:
                co+=1
        dic1.update({i:co})
    print(dic1)
except TypeError:
    print("Not a String")
except:
    print("Something went wrong")
