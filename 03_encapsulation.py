class Person:
    def __init__(self , name , age):
        self.name = name
        self.__age = age  #private property
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
    

p1 = Person("zahid" , 33)
print(p1.name)
#print(p1.age) # show error
print(p1.get_age())

p2 = Person("hassan ", -6)  
#p2.set_age(-3)
print(p2.get_age())