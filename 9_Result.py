# 9. create a python program to display  result enter 3 subject marks and find total an given result pass or fail
a = float(input("Enter J2EE Marks: "))
b = float(input("Enter Python Marks: "))
c = float(input("Enter CyberSecurity Marks: "))

if(a >= 35 and b >= 35 and c >= 35):
    print("Result Pass")
else:
    print("Result Fail")

result = a + b + c
print("Total: " , result)
