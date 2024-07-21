import Modules.Module_3_23 as f
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
choice = int(input("Enter Choice: "))

if(choice == 1):
    f.Addition(a,b)
elif(choice == 2):
    f.Subtraction(a,b)
elif(choice == 3):
    f.Multiplication(a,b)
elif(choice == 4):
    f.Division(a,b)
else:
    print("Enter only 1 to 4 number")