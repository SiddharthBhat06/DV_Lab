try:
    dic1={}
    a=input("Enter string :")
    for i in a.split(" "):
        co=0
        for j in a.split(" "):
            if i==j:
                co+=1
        dic1.update({i:co})
    print(dic1)
except TypeError:
    print("Not a String")
except:
    print("Something went wrong")
