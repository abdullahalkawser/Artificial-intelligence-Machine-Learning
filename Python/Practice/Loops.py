count = 0
# # while count < 10:
# #     print('lopppppppppp')
# #     count += 1

# #     print(((count)))

# '''print from 1 to 5,'''
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

#     print('enddddddd')


# '''print from 5 to 1,'''
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

'''Infinite Loop'''
# i = 1
# while i < 5:
#     print(i)




# First loop with break
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break  # loop stops when i is 5
    print('jj')
    i += 1

# Second loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # skips printing 3
    print(i)








    ''''for loop'''

for i in range(1, 6):  # from 1 to 5
    print(i)



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

else :
    print ('end loop')


numbwrs = [1,23,4,5,6,7,88,]    
for num in numbwrs:
    print(num)
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]

for i in range(1, 10, 2):
    print(i)