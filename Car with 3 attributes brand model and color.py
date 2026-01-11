# Define the Car class
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", "Red")

# Print the object attributes
print(my_car.brand)
print(my_car.model)
print(my_car.color)
