#Array Modification বলতে বোঝায়, একটি NumPy array তৈরি হওয়ার পর তার value পরিবর্তন করা, নতুন value যোগ করা, value মুছে ফেলা, replace করা বা update করা। array[index] = new_value

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print('original array:', a)

a[0] = 10 #index 0 er value 10  diye relace koira holo


print('array after modification:', a)




b = np.array([[1, 2, 3],
              [4, 5, 6]])

b[1, 1] = 6 #index (0,1) er value 10  diye relace koira holo Row 0, Column 1-এর value 2 ছিল।
# এখন 50 হয়েছে।

print('2D array after modification:', b)



# 2. Modify Multiple Values

# একসাথে অনেকগুলো value পরিবর্তন করা যায়।



c = np.array([1, 2, 3, 4, 5])

c[1:4] = 10 #index 1 theke 3 porjonto value 10 diye relace koira holo

c[1:4]= [10,20,30] #index 1 theke 3 porjonto value 10,20,30 diye relace koira holo

print('array after modifying multiple values:', c)


3. Boolean Modification

শর্ত অনুযায়ী value পরিবর্তন।

a = np.array([10,20,30,40,50])

a[a>30] = 0

print(a)
Output
[10 20 30 0 0]

ব্যাখ্যা:
৩০-এর বড় সব value 0 হয়ে গেছে।

Real Life Example

ধরো কোনো দোকানে ১০০০ টাকার বেশি ডিসকাউন্ট গ্রহণযোগ্য নয়।

discount[discount > 1000] = 1000
4. append()

শেষে নতুন element যোগ করা।

a = np.array([1,2,3])

b = np.append(a,4)

print(b)
Output
[1 2 3 4]

মনে রাখবে: append() মূল array পরিবর্তন করে না; নতুন array রিটার্ন করে।

5. insert()

নির্দিষ্ট index-এ value যোগ করা।

a = np.array([1,2,4])

b = np.insert(a,2,3)

print(b)
Output
[1 2 3 4]
6. delete()

কোনো element মুছে ফেলা।

a = np.array([10,20,30,40])

b = np.delete(a,2)

print(b)
Output
[10 20 40]
7. replace (Condition দিয়ে)

NumPy-তে replace() নামে কোনো function নেই। Condition ব্যবহার করে replace করা হয়।

a = np.array([10,20,30,20])

a[a==20] = 99

print(a)
Output
[10 99 30 99]
8. resize()

Array-এর size পরিবর্তন করা।

a = np.array([1,2,3,4])

a.resize((2,2))

print(a)
Output
[[1 2]
 [3 4]]
9. reshape()

Shape পরিবর্তন করা (Data একই থাকে)।

a = np.array([1,2,3,4,5,6])

print(a.reshape(2,3))
Output
[[1 2 3]
 [4 5 6]]
10. fill()

সব element একই value দিয়ে পূরণ করা।

a = np.array([1,2,3,4])

a.fill(5)

print(a)
Output
[5 5 5 5]
Real Life Example

একটি পরীক্ষার ফল প্রকাশের আগে সব ছাত্রের status "Pending" ধরে রাখতে চাই।

একইভাবে সব value একসাথে সেট করা যায়।

Interview / Exam Question
Question

Student-এর ৫টি মার্কস দেওয়া আছে।

[60,70,80,90,50]

যে মার্কস ৭০-এর কম, সেগুলোকে 0 করে দাও।

Solution
import numpy as np

marks = np.array([60,70,80,90,50])

marks[marks < 70] = 0

print(marks)
Output
[ 0 70 80 90  0]
Real-Life Uses
ক্ষেত্র	কীভাবে ব্যবহার হয়
Student Management	ভুল মার্কস update করা
Hospital	রোগীর রিপোর্ট update
Banking	Balance পরিবর্তন
E-commerce	Product price update
AI / Machine Learning	Dataset পরিষ্কার করা, ভুল data replace করা
Weather Analysis	Invalid temperature value replace করা
Employee System	Salary update করা
Summary Table
Function / Method	কাজ
a[index] = value	একটি value পরিবর্তন
a[start:end] = [...]	একাধিক value পরিবর্তন
a[condition] = value	শর্ত অনুযায়ী update
np.append()	শেষে নতুন value যোগ
np.insert()	নির্দিষ্ট index-এ value যোগ
np.delete()	value মুছে ফেলা
a.fill()	সব value একই করা
reshape()	Shape পরিবর্তন
resize()	Size পরিবর্তন
মনে রাখার সহজ ট্রিক
Modify → Value পরিবর্তন
Append → শেষে যোগ
Insert → মাঝখানে যোগ
Delete → মুছে ফেলা
Fill → সব একই value
Reshape → Shape পরিবর্তন
Resize → Size পরিবর্তন