class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy")
print(dog.speak())

class Runner:
    def run(self):
        return "Running fast."

class Swimmer:
    def swim(self):
        return "Swimming smoothly."

class Triathlete(Runner, Swimmer):
    def compete(self):
        return "Competing in a triathlon."

triathlete = Triathlete()
print(triathlete.run())
print(triathlete.swim())
print(triathlete.compete())

# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def get_model(self):
        return f"Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def get_battery(self):
        return f"Battery capacity: {self.battery_capacity} kWh"

electric_car = ElectricCar("Tesla", "Model S", 100)
print(electric_car.get_brand())
print(electric_car.get_model())
print(electric_car.get_battery())
