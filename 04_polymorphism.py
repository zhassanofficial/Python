class Vechile:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def move(self) :
        print("Vehile is moving")
class car(Vechile):
    def move(self):
        print("car is moving")
class boat(Vechile):
    def move(self):
        print("boat is sailing")
class Plane(Vechile):
    def move(self):
        print("flight is flying")

car1 = car("Toyota" , "corolla")
boat1 = boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")

for x in (car1 , boat1 , plane1):
    print(x.brand)
    print(x.model)
    x.move()
