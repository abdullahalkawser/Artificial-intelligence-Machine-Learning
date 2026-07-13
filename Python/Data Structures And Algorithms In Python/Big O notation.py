# Big O notation is a way to describe the performance or complexity of an algorithm in terms of time or space as the input size grows.
#  It provides an upper bound on the time or space required by an algorithm, allowing us to compare the efficiency of different algorithms.
# Big O Notation Examples

# Big O	বাংলা ব্যাখ্যা	উদাহরণ
# O(1)	ইনপুট যত বড় হোক, সময় একই থাকবে	অ্যারে থেকে ১ম আইটেম নেওয়া
# O(n)	ইনপুট যত বড়, সময় তত বাড়বে	লুপ চালিয়ে সব প্রিন্ট করা
# O(n²)	প্রতিটি উপাদানের সাথে আবার সব মিলানো	nested loop (প্রতিটি জোড়া প্রিন্ট)

def get_first_element(arr):
    return arr[0]

#  🎯 No matter how big the array is, you're just accessing the first element.

# 👉 Time doesn’t increase with input size → O(1)🎯 তুমি শুধু অ্যারের প্রথম উপাদান নিচ্ছো।
#🔍 ইনপুট ১০০ হোক বা ১০০০০, সময় একই — O(1)

#Example 2: O(n) - Linear Time
def print_all(arr):
    for item in arr:
        print(item)
#         🎯 এখানে তুমি প্রতিটি উপাদান একবার প্রিন্ট করছো।
# 🔍 যদি ৫টি উপাদান হয়, ৫ বার প্রিন্ট। ১০০ হলে, ১০০ বার।
# 👉 সময় বাড়ে ইনপুট অনুযায়ী — O(n)


# Example 3: O(n²) - Quadratic Time
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
# 🎯 এখানে তুমি প্রতিটি আইটেমের সাথে সবকিছুর জোড়া প্রিন্ট করছো।
# 🔍 যদি ৫টি উপাদান হয়, ৫x৫ = ২৫ বার লুপ চলবে।
# 👉 ইনপুট বেড়ে গেলে সময় অনেক বেশি বেড়ে যায় — O(n²)
