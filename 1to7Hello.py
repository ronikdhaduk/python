# 1. create a python program to hello world.
print("Hello world!")

# 2. create a python program to get two values from user and display the sum.
a = input("Enter number1: ")
b = input("Enter number2: ")
c = float(a) + float(b)
print("value of a is {0} and value of b is {1} sum is : {2} ".format(a,b,c))

# 3.create a python program using string and display output.
str1 = input("Enter your name: ")
str2 = input("Enter your surname: ")
str3 = str1 + str2
print("your full name is: ", str3)

str4 = "hello"
print(str4)

str5 = """hello all
        how are you?
        i am fine"""
        
print(str5)

str6 = 'Hello world!'
print(str6)

# 4. create a python program to check number = 10.
a = 10
if(a == 10):
    print(a)
print("this is out of if")

# 5.create a check given number is greter then 20 or less then 20
num1 = int(input("Enter number: "))
if(num1 > 20):
    print("number is greter then 20")
else:
    print("number is less then 20")

# 6.create to check given number 10 or greter then 20 or not
a = int(input("Enter number: "))
if(a == 10):
    print("value of a is 10")
elif(a > 20):
    print("value of a is greter then 20")
else:
    print("value of a is  less then 20")

# 7. cretae a python program to genrate PGVCL bill amount. price(1 to 100 = 4, 100 to 200 = 4.5, 200 to onwords = 5)
unit = float(input("Enter Your Unit: "))
if(unit > 0 and unit <= 100):
    amount = unit * 4
    print("Amount is: ",amount)
elif (unit > 100 and unit <= 200):
    amount = unit * 4.5
    print("Amount is: ", amount)
else:
    amount = unit * 5
    print("Amount is: ", amount)
    
    