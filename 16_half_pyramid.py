# 16. display following pattern
# *  
# *  *  
# *  *  *  
# *  *  *  *  
# *  *  *  *  * 
rows = int(input("Enter numbers of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("* ", end=" ")
    print()