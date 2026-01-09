# родительский, суперкласс
class Car:
    def __init__(self, model, color):
        self.color = color
        self.model = model
        self.speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}.")
# дочерний, подкласс
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Bus {self.model} driving to", destination)

class Truck(Car):
    def drive_to(self, destination):
        print(f"Truck driving to", destination)

bus = Bus("Mercedes", "red", 42)
truck = Truck("MAN", "white")
car = Car("Subaru", "red")
vehicles = (bus, truck, car)
for v in vehicles:
    v.drive_to("Bishkek")