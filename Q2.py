def prime():
    to=0
    try:
        a=int(input("Enter number :"))
        for i in range(2,a):
            if a%i==0:
                to=1
                break
        if to==1:
            print("False")
        else:
            print("True")

    except:
        print("Oops something went wrong!")
prime()