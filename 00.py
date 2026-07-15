class person:
    def __init__(self, name , age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def display(self):
        print(f"Hi I'm {self.name} and I'm {self.get_age()} year old ")
    @staticmethod
    def Greet():
        print("hello Good evening")   # Does not need the self parameter

p = person("zahid" , 21)
p.display()
print(p.name)
person.Greet()