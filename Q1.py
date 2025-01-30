def calculator():
    print("Python Calculator")
    try:
        a= eval(input("Enter Number 1 :"))
        b= eval(input("Enter Number 2 :"))
        c= int(input("Enter choice of operation : 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division"))
        if c in range(1,5):
            if c==1:
                print("Sum is :",a+b)
            elif c==2:
                print("Difference is :",a-b)
            elif c==3:
                print("Product is :",a*b)
            elif c==4:
                print("Quotient is :",a/b)


    except:
        print("Invalid input")