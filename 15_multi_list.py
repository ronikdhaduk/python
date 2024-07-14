# 15. create a python program to display elements of multiple list

list1 = ['i am ', 'you are ']
list2 = ['fine', 'well', 'good']

list_size = len(list2)

for item in list1:
    i = 0
    while(i < list_size):
        print(item, list2[i])
        i += 1
    print()
    