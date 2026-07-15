from abc import ABC , abstractmethod
class vechile(ABC):
    @abstractmethod
    def move(self):
        pass
class car(vechile):
    def move(self):
        print("car is moving")
class boat(vechile):
    def move(self):
        print("boat is sailing")

c1 = car()
c1.move()

b1 = boat()
b1.move()



'''
Vehicle defines a blueprint for all vehicles (must have a move() method).
Subclasses like Car and Boat must implement the move() method.
You can’t create an object of Vehicle directly — it’s abstract.
'''