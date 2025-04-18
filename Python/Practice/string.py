str1= 'abdullahhhhh'
str2 = 'software Engineer'

print( len (str1 + '' + str2))

 

abd = 'abdullah al kawser'
print(len(abd))

abd = 'abdullah al kawser'
print(abd[12])
print(abd.index('k'))  # Output: 0 (first 'a' is at index 0)

'''Python Slicing Basic Syntax:'''

name = "abdullah al kawser"
print(name[0:8])     # Output: 'abdullah প্রথম ৮টা অক্ষর: (default: 1)'
print(name[9:11])    # Output: 'al  শুধু 'al' বের করতে:'
print(name[-6:])     # Output: 'kawser ৩. শেষে ৬ অক্ষর:'
print(name[0:8:2])   # Output: 'adlah মাঝখান থেকে শুরু করে skip করে বের করা:' (0→2→4→6)
print(name[::-1])    # Output: 'reswak la halludba  পুরো string reverse করে দেখা:'


quote = "Python is powerful!"

print(quote[9:15])  
print(quote[14:19])  
print(quote[::-1])  


fruits = ["apple", "banana", "cherry", "mango", "pineapple"]

print(fruits[0:3])   # ['apple', 'banana', 'cherry']
print(fruits[-2:])   # ['mango', 'pineapple']
print(fruits[::2])   # ['apple', 'cherry', 'pineapple']
print(fruits[::-1])  # ['pineapple', 'mango', 'cherry', 'banana', 'apple']






