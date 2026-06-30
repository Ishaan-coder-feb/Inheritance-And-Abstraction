from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def speak(self):
        pass
class dog(animal):
    def __init__(self,name,age,breed):
        self.breed=breed
        super().__init__(name,age)
    def speak(self):
        print(self.name,"shouts woof woof and barks")
class lion(animal):
    def __init__(self,name,age,colour):
        self.colour=colour
        super().__init__(name,age)
    def speak(self):
        print(self.name,"roars!")
class horse(animal):
    def __init__(self,name,age,speed):
        self.speed=speed
        super().__init__(name,age)
    def speak(self):
        print(self.name,"shouts neigh negih")
d=dog("Coco",5,"Golden Retriever")
d.speak()
l=lion("Simba",12,"yellowish brown")
l.speak()
h=horse("Jofra",9,67)
h.speak()
    
    
    
    

        
 
