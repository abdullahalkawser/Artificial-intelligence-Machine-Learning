# Creating a dictionary is mutable chnage kora jabe



student = {
    "name": "Anisa",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.5
}

# Accessing values
print(student["name"])       # Output: Anisa
print(student["cgpa"])       # Output: 3.5
print(student["department"])  


# Add a new key-value pair
student["name"] = 'abdullaha al kawser'
student["semester"] = 10;

# Update an existing value
student["cgpa"] = 3.23

# Delete a key-value pair
del student["age"]


print(type(student))

print(student)


''': Student Records (Nested Dictionary)'''

students = {
    "101": {
        "name": "abdullah",
        "department": "CSE",
        "cgpa": 3.8
    },
    "102": {
        "name": "Rafi hassan"
        "",
        "department": "EEE",
        "cgpa": 3.6
    }
}

# Accessing data
print(students["101"]["name"])      # Output: Anisa
print(students["102"]["cgpa"])      # Output: 3.6



'''Common Dictionary Methods'''

student = {
    "name": "Anisa",
    "age": 22,
    "department": "CSE"
}

# keys()
print(student.keys())        # dict_keys(['name', 'age', 'department'])

# values()
print(student.values())      # dict_values(['Anisa', 22, 'CSE'])

# items()
print(student.items())       # dict_items([('name', 'Anisa'), ('age', 22), ('department', 'CSE')])

# get()
print(student.get("name"))   # Anisa
print(student.get("cgpa", "Not found"))  # Not found (default value if key doesn't exist)

# update()
student.update({"cgpa": 3.8, "age": 23})
print(student)

# pop()
student.pop("department")    # Removes 'department'
print(student)

# copy()
new_student = student.copy()
print(new_student)

# clear()
student.clear()
print(student)               # {}



'''' Set?
A set is an unordered collection of unique elements.
It's defined using curly braces {} or the set() function.'''

fruits = {"apple", "banana", "cherry", "banana",'mango', 'green coconusts'}
print(fruits)  # Output: {'apple', 'banana', 'cherry'} — duplicates removed

# You can also create an empty set like this:
empty_set = set()  # NOT empty_set = {} (that's a dict!)

my_set = {1, 2, 3}

my_set.add(4)
print(my_set)   # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set)   # Output: {1, 3, 4}

my_set.discard(10)  # No error


item = my_set.pop()
print("Removed:", item)
print(my_set)

my_set.clear()
print(my_set)   # Output: set()


original = {1, 2, 3}
copied = original.copy()
print(copied)   # Output: {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # Output: {1, 2, 3, 4, 5}

print(a.intersection(b))  # Output: {3}


print(a.difference(b))  # Output: {1, 2}

x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True



