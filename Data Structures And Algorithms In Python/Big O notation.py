# Big O notation is a way to describe the performance or complexity of an algorithm in terms of time or space as the input size grows.
#  It provides an upper bound on the time or space required by an algorithm, allowing us to compare the efficiency of different algorithms.
# Big O Notation Examples

def get_first_element(arr):
    return arr[0]

#   🎯 No matter how big the array is, you're just accessing the first element.

# 👉 Time doesn’t increase with input size → O(1)

#Example 2: O(n) - Linear Time
def print_all(arr):
    for item in arr:
        print(item)


# Example 3: O(n²) - Quadratic Time
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)