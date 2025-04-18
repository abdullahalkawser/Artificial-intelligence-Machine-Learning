# ==	Equal to !=	Not equal to  >	Greater than  <	Less than  >=	Greater than or equal to <=	Less than or equal to

print(10 == 10)  # True
print(10 == 5)   # False
print("hello" == "hello")  # True

print(10 > 5)  # True
print(3 > 8)   # False

print(8 < 3)   # False

a = 20
b = 15

print(a > b)   # True
print(a == b)  # False
print(a != b)  # True
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    

    print("apple" == "apple")  # True
print("apple" > "banana")  # False (because 'a' comes before 'b' in ASCII)
print("car" < "dog")  # True

x = 10

print(5 < x < 15)  # True (same as 5 < x and x < 15)
print(5 < x > 8)   # True (same as 5 < x and x > 8)