class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

car1 = Car("Toyota", "Red")

car1.display_info()

car1.color = "Blue"

car1.display_info()

car2 = Car("Mitsubishi", "Black")

car2.display_info()