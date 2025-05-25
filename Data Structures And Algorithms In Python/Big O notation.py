# 1. O(1) — Constant Time
# Runs in the same time regardless of input size.

def constant_time(arr):
    return arr[0]  # Always takes 1 step

#2. O(n) — Linear Time
#Time grows linearly with input size.
def linear_time(arr):
    for item in arr:
        print(item)  # One step per item

# O(n²) — Quadratic Time
# Nested loops — time grows with square of input size.
def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # n * n steps


# O(log n) — Logarithmic Time
# Input size is reduced by half each time (like binary search).
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# O(n log n) — Linearithmic Time
# Efficient sorting algorithms like mergesort, quicksort. 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



# ✅ Summary Table
# Big O	Name	Example
# O(1)	Constant	Accessing arr[0]
# O(n)	Linear	Loop through list
# O(n²)	Quadratic	Nested loop
# O(log n)	Logarithmic	Binary search
# O(n log n)	Linearithmic	Merge sort, quicksort