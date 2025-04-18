# def function_name(parameters):
#     # code to be executed
#     return result  # optional


def greet(name):
    print("Hello, " + name + "!")

greet("abdullah al akawser")  # Calling the function


def abdul (names,job):
    print('Hellow ' + names , 'he is best ' + job)
abdul('kawser','software Engineer')     
abdul('kawserkstps','software Engineer and data scince')  
abdul('kawserssssssssss','software Engineersssssssssssss')  


def sumNumber (a,b,c):
   sum =(a+b+c)
   print(sum)
   return sum
sumNumber(20,3,4 )    

''' Function with Default Parameter'''
def greet(name="Anisa"): 
    print("Hello,", name)

greet()          # uses default
greet("Rahman")  # overrides default


''' Nested Function (Function inside another function)'''

def outer():
    def inner():
        print("I am inner!")
    print("I am outer!")
    inner()

outer()



'''print list '''
city = ['Rangpur', 'Dhaka', 'Chattogram']
country = ['Bangladesh', 'Bangladesh', 'Bangladesh','Bangladesh', 'Bangladesh', 'Bangladesh']

def printlenth(list):
    print(len(list))

printlenth(city)
printlenth(country)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))


def contertaka (usdval):
    takavalue= usdval *120
    print(takavalue,usdval)

contertaka(100)

'''recursion'''
def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(10)    
