# 8. create a python program to get 3 numbers and find greater number
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
if(a > b):
    if(a > c):
        print("a is Greater")
    else:
        print("c is Greater")
elif(b > c):
    if( b > a):
        print("B is greater")
    else:
        print("a is greater")
else:
    print("c is greater")