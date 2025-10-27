# 1. Basic Class And Object Creation

# Define a class named 'Car' with attributes 'brand' and 'model'. Then create an object of this class. 

class Car:
     def __init__ (self, userbrand, usermodel):
          self.brand = userbrand
          self.model = usermodel

my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla

my_new_car = Car("Tata", "Safari")

# __init__ -----> constructor method which is called when an object of the class is created.

# self -----> represents the instance of the class. It is used to access variables that belongs to the class.


