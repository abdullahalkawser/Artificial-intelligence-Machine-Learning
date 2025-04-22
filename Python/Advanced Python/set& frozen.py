# Creating a set
my_set = {1, 2, 3, 4, 5, 2, 3}
print(my_set)  # Output: {1, 2, 3, 4, 5} — duplicates removed

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}


