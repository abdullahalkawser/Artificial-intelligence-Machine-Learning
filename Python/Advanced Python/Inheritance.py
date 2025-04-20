class Vehicle:
    def uses(self):
        print('Using general transport form every day')

class Car(Vehicle):
    def __init__(self):
        print('I am car')
        self.wheel = 4  
        self.sunroof = True 

    def specific_uses(self):
        self.uses()  # Call parent method
        print('I am a car, used to drive all family members')

class Bike(Vehicle):
    def __init__(self):
        print('I am bike')
        self.wheel = 2  
        self.sunroof = False

    def specific_uses_bike(self):
        self.uses()  # Call parent method
        print('I am a biker, used for racing')

# Create object of Car
c = Car()
# c.specific_uses()   # Call method from Car

# # Create object of Bike
b = Bike()
b.specific_uses_bike()  # Call method from Bike


# print(isinstance(c, Car))      # ✅ True  # Bike is NOT a Car → True
# print(isinstance(c, Vehicle))  # ✅ True
# print(isinstance(c, Bike))     # ❌ False  # Bike is NOT a Car → False

print(issubclass(Car, Vehicle))    # ✅ True




print(issubclass(Car, Bike))   # ❌ False
print(issubclass(Car, object)) # ✅ True (because everything in Python inherits from 'object')


# print(isinstance(b, Bike))      # ✅ True  # Bike is a Vehicle → True
# print(isinstance(b, Vehicle))  # ✅ True
# print(isinstance(b, Car)) 
print(issubclass(Bike, Vehicle))   # ✅ True



#  Multiple Inheritance Example (with full comments)
# Parent class 1
class Father:
    def skills(self):
        print("Father: Cooking, Driving")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Painting, Singing")

# Child class inherits from both Father and Mother
class Child(Father, Mother):  # 👉 Multiple Inheritance
    def skills(self):
        print("Child: Python Programming")  # Own method
        Father.skills(self)  # 👉 Explicitly calling Father's skills()
        Mother.skills(self)  # 👉 Explicitly calling Mother's skills()

# Creating object of Child class
c = Child()

# Calling the skills method
c.skills()

