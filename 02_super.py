class employee:
    def __init__(self):
        print("constructor of employee")
    a = 1
class programmer(employee):
    def __init__(self):
        super().__init__()
        print("constructor of programmer")

    b = 2
class cooder(programmer):
    def __init__(self):
         super().__init__()
 
         print("constructor of cooder")
    c = 3
        
        
#obj1 = employee()
#print(obj1.a)

#obj2 = programmer()
#print(obj2.a , obj2.b)

obj3 = cooder()
print(obj3.a , obj3.b , obj3.c)