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


# Creating a frozenset
fset = frozenset([1, 2, 3, 4, 4, 5])
print(fset)  # Output: frozenset({1, 2, 3, 4, 5})

# Try to add (will raise error)
# fset.add(6)  # ❌ AttributeError

# Set operations still work
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a.union(b))        # frozenset({1, 2, 3, 4, 5})
print(a.intersection(b)) # frozenset({3})
print(a.difference(b))   # frozenset({1, 2})
