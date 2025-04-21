my_list = [10, 20, 30,100,20,3,4,9999]
my_iter = iter(my_list)  # Create iterator
myl=reversed(my_list)

dir(my_list)

print(next(myl))  # 100

# for i in my_list:
#     print(i)

my_string = "Anisa"
my_iters = iter(my_string)

print(next(my_iters))  # A
print(next(my_iters))  # n

print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
print(next(my_iter))  # 30



#print(next(my_iter))  # Will raise StopIteration


#: Custom Iterator Class
#__iter__() → returns the iterator object itself

#__next__() → returns the next value



class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

# Use it
my_counter = Counter(1, 5)
for number in my_counter:
    print(number)
