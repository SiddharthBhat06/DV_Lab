a=eval(input("Enter a tuple having 5 elements :"))
try:
    a[0]=10
except TypeError:
    print("Since a tuple is an immutable datatype it's data cannot be changed. Therefore it raises a TypeError which is handled by the except block")
