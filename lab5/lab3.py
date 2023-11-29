class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self):
        return f"This car has a fuel efficiency of {self.fuel_efficiency} miles per gallon."

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon):
        super().__init__(make, model, year)
        self.miles_per_gallon = miles_per_gallon

    def calculate_mileage(self):
        return f"This motorcycle has a mileage of {self.miles_per_gallon} miles per gallon."

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"This truck has a towing capacity of {self.towing_capacity} pounds."


car = Car("Audi", "A6", 2022, 30)
motorcycle = Motorcycle("Honda", "Sport", 2021, 50)
truck = Truck("Mercedes", "ModelX", 2023, 10000)

print(car.make)
print(car.calculate_mileage())
print(motorcycle.make)
print(motorcycle.calculate_mileage())
print(truck.make)
print(truck.calculate_towing_capacity())
