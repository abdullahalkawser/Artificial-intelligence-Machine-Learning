name = 'abdullah';
age = 23;

male = True;


print('My Name is :', type (name), 'age:',type(age),'Gender:' , type(male))



''' conditional statement'''

light = input('Light :')

if(light == 'red'):
    print('stop')
elif(light == 'yellow'):
    print('wait')      
elif(light == 'green'):
    print('gooooo')  
else:
    print('you must wait  for traficc')   

'''ternary operator '''
light = input('Light: ')
print('stop' if light == 'red' else 'wait' if light == 'yellow' else 'gooooo' if light == 'green' else 'you must wait for traffic')

 
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

'''logical operation'''

print(not False)
print(not True)


ball = True;
ball2 = False

print(ball and ball2); ''''2 tai ture hote hbe '''


ball = True;
ball2 = False

print(ball or ball2); ''''1 tai ture hote hbe '''

'''type conversion '''
age = '23'
nim = 29.89

agess = int(age)
prin = int(nim)

print(type(prin))    # <class 'int'>
print(type(age))     # <class 'str'>
print(type(agess))   # <class 'int'>


a = int(input("Enter a number: "))
b = float(input("Enter a decimal: "))
print(a + b)

