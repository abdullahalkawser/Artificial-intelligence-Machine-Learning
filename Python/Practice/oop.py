class Person:
    def __init__(self, name, age):  # Constructor with parameters
        self.name = name            # Assign name to the object
        self.age = age              # Assign age to the object

    def speak(self):                # Method to speak
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
dogs = Person('abdullah', 38)

# Calling the method
dogs.speak()




class Student:
    def __init__(self,name,age,job):
        self.name= name
        self.age = age
        self.job = job

    def hellow(self):
        print('Hi ',self.name,'age',self.age,'job Psossion ',self.job)   
hi = Student('abdullah',23,'djjdjdjdjj')
hi.hellow( )


''' static method'''

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Call static methods using the class name (no need to create an object)
print(Calculator.add(10, 5))        # Output: 15
print(Calculator.multiply(4, 3))    # Output: 12
''' Abstraction – Hide complex implementation and show only the essentials'''

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# obj = Animal()  ❌ Can't create object of abstract class
d = Dog()
d.make_sound()  # Output: Woof!


'''Encapsulation – Keep data safe from outside access using private/protected members'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
# print(acc.__balance)    ❌ Error: can't access private variable


'''Inheritance – One class inherits features of another class'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):  # Inheriting from Vehicle
    def drive(self):
        print(f"{self.brand} is driving...")

my_car = Car("Toyota")
my_car.start()  # Output: Toyota is starting...
my_car.drive()  # Output: Toyota is driving...


'''Polymorphism – Same method name behaves differently in different classes'''
class Bird:
    def fly(self):
        print("Some birds can fly")

class Parrot(Bird):
    def fly(self):
        print("Parrot can fly high")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def bird_fly_test(bird):
    bird.fly()

bird_fly_test(Parrot())   # Output: Parrot can fly high
bird_fly_test(Penguin())  # Output: Penguin can't fly



''' Delete an object attribute'''
class MyClass:
    def __init__(self):
        self.a = 5
        self.b = 10

obj = MyClass()
del obj.a
# print(obj.a)  # ❌ Error: 'MyClass' object has no attribute 'a'




'''Modifier	Syntax	Meaning / Access

Public	name	Fully accessible everywhere
Protected	_age	Internal use, accessible in subclasses
Private	__salary	Only inside class (name mangling used)

'''

'''Public Members'''

class Person:
    def __init__(self, name):
        self.name = name  # public variable

p = Person("Anisa")
print(p.name)  # ✅ Output: Anisa


'''Private Members
Declared by prefixing with double underscore (__)

Not accessible directly from outside the class

Used to hide sensitive data'''

class Person:
    def __init__(self, name, age):
        self.name = name         # public
        self.__age = age         # private

    def show(self):
        print(f"Name: {self.name}, Age: {self.__age}")

p = Person("Anisa", 22)
p.show()               # ✅ Output: Name: Anisa, Age: 22
# print(p.__age)       # ❌ Error: 'Person' object has no attribute '__age'

# If needed, still accessible (not recommended)
print(p._Person__age)  # ⚠️ Output: 22 (name mangling)

'''Protected Members in Python
Defined with a single underscore prefix: _variable

It’s a convention (not a strict rule):
➤ "You shouldn't access this from outside the class directly."
➤ But Python doesn’t stop you from doing it.

Used when:

You want to indicate that something is meant for internal use.

But it can be accessed by subclasses if needed.'''


class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self._age = age           # protected

    def display(self):
        print(f"Name: {self.name}, Age: {self._age}")

class Student(Person):
    def show_age(self):
        print(f"Accessing protected age: {self._age}")  # allowed

s = Student("Anisa", 22)
s.display()           # ✅ Output: Name: Anisa, Age: 22
s.show_age()          # ✅ Output: Accessing protected age: 22

# Direct access (not recommended, but possible)
print(s._age)         # ⚠️ Output: 22

