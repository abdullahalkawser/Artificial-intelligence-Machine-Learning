x = 5  # int
y = 3.14  # float

print(x,y)

# Creating boolean variables
a = True
b = False

print(a)  # Output: True
print(b)  # Output: False

print('Hellow worlds')

# String Operations:


#1. Concatenation:

first_name = "Abdullah"
last_name = "Al Abdullah"
full_name = first_name + " " + last_name
print(full_name)  # Output: Abdullah Al Abdullah

#2. Repetition:

name = 'abdullah'
names_repeat = (name + ' ') * 10  # Add a space after the name and repeat it 10 times
names_repeat = names_repeat.strip()  # Remove the extra space at the end
print(names_repeat)

#3. Accessing Characters:
word = "Python"
print(word[0])  # Output: P (first character)
print(word[2])  # Output: t (third character)

#4. Slicing Strings:
word = "Python"
print(word[0:])
print(word[:])  # Copy all characters
print(word[:3])  # Output: Pyt (characters from index 0 to 2)

print(word[1:4])  # Output: yth (characters from index 1 to 3)

#5. String Length:
word = "Python"
print(len(word))  # Output: 6

#6. String Methods:

sentence = "   Hello, World!   "
print(sentence.lower())  # Output: hello, world!
print(sentence.upper())  # Output: HELLO, WORLD!
print(sentence.strip())  # Output: Hello, World!
print(sentence.find("Hello"))
print(sentence.replace("World", "Python"))  # Output: Hello, Python!
words = sentence.split(",")
print(words)  # Output: ['Hello', ' World!   ']


#7. String Formatting:

name = "Alice"
age = 30
sent = "name : " + name + ",age: " + str(age);
print(sent)

#Using f-strings (Python 3.6+):
name = "Alice"
age = 30
sentence = f"Name: {name}, Age: {age}"
print(sentence)  # Output: Name: Alice, Age: 30

#Using .format() method:
name = "Alice"
age = 30
sentence = "Name: {}, Age: {}".format(name, age)
print(sentence)  # Output: Name: Alice, Age: 30

#Escape Characters:
quote = "She said, \"Hello!\""
print(quote)  # Output: She said, "Hello!"

#Multiline Strings:
multi_line_string = """This is a string
that spans multiple lines."""
print(multi_line_string)
# Output:
# This is a string
# that spans multiple lines.


