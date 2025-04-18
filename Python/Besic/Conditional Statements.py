
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#if-elif-else (Multiple Conditions)
    marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

    #if Statement with User Input
    number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

#Ternary Operator

#condition ? value_if_true : value_if_false  : value_if_true if condition else value_if_false

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Even


#Logical Operators pythn and Operator:

x = 10
y = 5
result = (x > 5) and (y < 10)
print(result)  # True, because both conditions are True

x = 10
y = 15
result = (x > 5) or (y < 10)
print(result)  # True, because one condition is True

x = 10
result = not (x < 5)
print(result)  # True, because x < 5 is False, so not False becomes True

x = 10
y = 5
z = 20
result = (x > 5) and (y < 10) or (z == 20)
print(result)  # True, because (x > 5) and (y < 10) is True, so True or (z == 20) becomes True
