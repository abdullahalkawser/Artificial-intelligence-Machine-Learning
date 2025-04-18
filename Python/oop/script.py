# name = 'abdullah';
# age = '38';
# print(name, age);
# print(type(name), type(age));

# # declare create a class


# class Person:
#     def __init__(self, name, age):  # Correct attribute names
#         self.name = name  
#         self.age = age  

#     def speak(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Correct way to create an object
# dogs = Person('abdullah', 38)  # Separate name and age


# # Printing attributes
# print(dogs.name, dogs.age)  # This will print: abdullah 38

# # Calling the method
# dogs.speak()  # Output: Hello, my name is abdullah and I am 38 years old.


# class Person:
#     def __init__(self,name,age):
#         self.nam = name;
#         self.ag = age;
      

#     def bark(self):
#         print('whoof whoof');

# dogs = Person('abdullah, 38');
# print(dogs.name,dogs.age);
# dogsas = Person('kawser, 80');
# print(dogsas.name,dogsas.age);
# # dog.bark();


# Combining objects
# class Dogs:
#     def __init__(self, name, age, color, owner):
#         self.name = name #storing value
#         self.age = age
#         self.color = color
#         self.owner = owner  # Correctly assign the owner object

#     def bark(self): # defining methon
#         print('whoof whoof')

# class Owner:
#     def __init__(self, name, address, number):
#         self.name = name
#         self.address = address
#         self.number = number

# # Correct variable name and instantiation
# owner = Owner('Abdullah', 'Dhaka', 847755)

# # Pass the 'owner' object without parentheses
# person = Dogs('Kawser', 30, 'black', owner)
# person3 = Dogs ('abdullah al kawser',46,'red')
# print(person.owner.name)
# person2 = Dogs('hassan', 31, 'red', owner)

# # Print details
# print(person.name, person.age, person.color)
# print(person2.name,person2.age)
# person.bark()


#  Accessing Object Data
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# # Creating an object
# mycar = Car('lamborgini','corola', 20330) 

# # Accessing attributes
# print (mycar.brand)  # Output: Toyota
# print(mycar.model)  # Output: Corolla
# print(mycar.year)   # Output: 2020

# #Modifying Object Data
# mycar.year = 20203
# print(mycar.year)


class Parent:
    def __init__(self,name,age ):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute

    def show_info(self):
      print(f"Name: {self.name}, Age: {self._age}")

# Creating an object
p = Parent("Alice", 25)
p.show_info()  # Output: Name: Alice, Age: 25

# Modifying protected attribute directly (Not recommended)
p._age = 200
print(p._age)  # Output: 25

# Accessing protected attribute (Not recommended, but possible)
print(p._age)  # Output: 25;


#  Using Methods to Access and Modify Data

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_year(self):
        return self.year  # Getter method

    def set_year(self, new_year):
        if new_year >= 1886:  # Validating before modifying
            self.year = new_year
        else:
            print("Invalid year!")

# Creating an object
my_car = Car("Toyota", "Corolla", 2020)

# Using getter and setter
print(my_car.get_year())  # Output: 2020
my_car.set_year(2025)     # Modifying with setter
print(my_car.get_year())  # Output: 2025

# Modifying Private Attributes with Getters and Setters


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

# Creating an object
account = BankAccount(1000)

# Accessing private attribute via getter
print(account.get_balance())  # Output: 1000

# Modifying private attribute via method
account.deposit(500)
print(account.get_balance())  # Output: 1500


#  Using @property for Read-Only Access
class Car:
    def __init__(self, brand, model, year):
        self._year = year  # Using single underscore to indicate it's a "protected" attribute

    @property
    def year(self):
        return self._year  # Read-only property

# Creating an object
my_car = Car("Toyota", "Corolla", 2020)

# Accessing like an attribute
print(my_car.year)  # Output: 2020

# Trying to modify (will raise an error)
# my_car.year = 2025  # AttributeError: can't set attribute



# Python's "Consenting Adults" philosophy and private attributes
class Person:
    def __init__(self, name, age):
        self.name = name      # Public
        self._age = age       # Protected (convention)
        self.__salary = 5000  # Private (name mangling applied)

    def show_salary(self):
        print(f"Salary: {self.__salary}")  # Accessing within class

# Creating an object
p = Person("Alice", 30)

# Public access
print(p.name)   # ✅ Allowed (Output: Alice)

# Protected access (not recommended but possible)
print(p._age)   # ✅ Allowed (Output: 30)

# Private access (will raise an AttributeError)
# print(p.__salary)  # ❌ AttributeError

# But can still access using name mangling (not recommended)
print(p._Person__salary)  # ✅ Allowed (Output: 5000)

