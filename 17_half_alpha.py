# 17. display following pattern
# A
# B C
# D E F
# G H I J
# K L M N O

rows = int(input("Enter number of rows: ")) 
ascii_value = 65
for i in range(rows):
    for j in range(i + 1):
        alphabat = chr(ascii_value)
        print(alphabat, end=" ")
        ascii_value += 1
    print()
    
# 18.Task : display following pattern
# A
# A B 
# A B C
# A B C D
# A B C D E

rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i + 1):
        alphabat_value = chr(ascii_value)
        print(alphabat_value, end=" ")
        ascii_value += 1
    ascii_value = 65
    print()
    