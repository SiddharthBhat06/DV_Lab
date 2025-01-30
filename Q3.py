def seq():
    sum=0
    try:
        for i in range(1,101):
            if i%2!=0:
                print(i)
            else:
                sum+=i
        print("\n\n",sum)
    except:
        print("Oops ran into a problem")

seq()