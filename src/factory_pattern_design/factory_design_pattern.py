from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def __init__ (self) -> None:
        super().__init__()
        
    @abstractmethod  
    def deliver(self):
        pass
    
class TransportFactory:
    @staticmethod
    def create_transport(transport_type, capacity):
        if transport_type == "truck":
            return Truck(capacity)
        elif transport_type == "ship":
            return Ship(capacity)
        else:
            raise ValueError("Invalid Transport Type") 
    
class Truck(Transport):
    def __init__(self, capacity):
        super().__init__()
        self.__capacity = capacity
        
    def getCapacity(self):
        return self.__capacity
        
    def deliver(self):
        return f"Delivering goods by road using a truck with capacity: {self.getCapacity()}!"
    
class Ship(Transport):
    def __init__(self, tonnage):
        super().__init__()
        self.__tonnage = tonnage
        
    def getTonnage(self):
        return self.__tonnage
    
    def deliver(self):
        return f"Delivering goods by sea using a ship with tonnage {self.getTonnage()}!"
    

try:
    truck = TransportFactory.create_transport("truck", 20)
    print(truck.deliver())
    
    ship = TransportFactory.create_transport("ship", 40)
    print(ship.deliver())
    
    car = TransportFactory.create_transport("car", 100)
    print(car.deliver())
    
except ValueError as e:
    print(f"Caught Error: {e}")




    
        


