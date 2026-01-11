class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} {self.model} accelerates to {self.speed} km/h")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"{self.brand} {self.model} slows down to {self.speed} km/h")

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} | Speed: {self.speed} km/h")


# Creating multiple Car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)
car3 = Car("Ford", "Mustang", 2019)

# Calling methods on each object
car1.display_info()
car1.accelerate(30)
car1.brake(10)

car2.display_info()
car2.accelerate(60)

car3.display_info()
car3.accelerate(50)
car3.brake(20)
