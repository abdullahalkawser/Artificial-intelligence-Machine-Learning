# Data Types in Python

# integer (init);



age = 25;

print("Age:", age)
print("type of age:", type(age));
print("Age:", age)






#Float (float);

price = 18.90;

print("Price:", price);
print("type of price:",type(price))

print("Price:", price)




#String (str);



name = "Alice";
name = 'Alice';
print("Name:", name);
print("type of name:", type(name));


#boolean (bool);

cofeeis_Hot= True;

coffeeis_Cold= False;

print("Coffee is Hot:", cofeeis_Hot);
print("type of cofeeis_Hot:", type(cofeeis_Hot));


print("Coffee is Cold:", coffeeis_Cold);
print("type of coffeeis_Cold:", type(coffeeis_Cold));





#list 

colors = ["red", "green", "blue"];


colors [0] = "yellow";  # changing the first element of the list


print(colors[0]);  # Output: yellow
print(colors[-1]);  # Output: blue last value of the list
print("Colors:", colors);
print("type of colors:", type(colors));



#naming convention for sring variable  multi-line string


description = '''This is a descriptionTuple হলো
 Python-এর একটি ordered এবং
  immutable (পরিবর্তন করা যায় না) data type। 
  একবার Tuple তৈরি করলে এর element পরিবর্তন, যোগ বা মুছে ফেলা যায় না।

''';

print("Description:", description);
print("type of description:", type(description));




# Dictionary


person = {
    "name": "abdullah",
    "age": 30,
    "department": "cse",
}

print("person: ",person);
print("type of person:", type(person));





#tupleTuple in Python

# Tuple হলো Python-এর একটি ordered এবং immutable (পরিবর্তন করা যায় না) data type। একবার Tuple তৈরি করলে এর element পরিবর্তন, যোগ বা মুছে ফেলা যায় না।




fruits = ("Apple", "Banana", "Mango")
print(fruits);
print("type of fruits:", type(fruits));
fruits = ("Apple", "Banana", "Mango")
print(len(fruits))

# Element Access করা
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)