def Outer():
    a = 10 #Local Scope
    def Inner():
        b = 20   #Local Scope
        print("a is : ", a)
        print("b is : ", b)
    Inner()
Outer() 