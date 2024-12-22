class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car("Toyota", "Fortuner", "Gasoline")

motorcycle = Motorcycle("Yamaha", "Fazzio", "Gasoline")

car.describeVehicle()
motorcycle.describeVehicle()