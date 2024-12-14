from abc import ABC , abstractmethod

class animal(ABC):
    def move(self):
        pass

class fish(animal):
    def move(self):
        print("Fishes move by swimming!!!!!!!!!!!!!")

class bird(animal):
    def move(self):
        print("Birds flyyyyyyyyyyy")
    
f1 = fish()
f1.move()

b1 = bird()
b1.move()












