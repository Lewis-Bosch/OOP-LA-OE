class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

washing_machine = WashingMachine("LG", "Topload2024")
refrigerator = Refrigerator("Samsung", "SM29ls90")
microwave = Microwave("Panasonic", "PNl0882")

appliances = [washing_machine, refrigerator, microwave]

for appliance in appliances:
    appliance.operate()
    appliance.info()