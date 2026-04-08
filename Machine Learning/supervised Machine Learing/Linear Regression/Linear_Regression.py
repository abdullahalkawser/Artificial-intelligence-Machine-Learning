# # # Linear Regression

# # # 1 finds pattern in olid datas

# # # 2 staright line
# # # 3 line 
# # # 4 formula : y = mx + c // y = predicted value m = slope of the line , x = input value , c = intercept of the line 



# # from sklearn.linear_model import LinearRegression

# # x = [[2, [3], [4], [5], [6]] # 2d array of study_hours
# # y = [50, 60, 70, 80, 90] # 1d array of scores

# # # // model objcet তৈরি করা হয়েছে
# # model = LinearRegression() 

# # #// model কে train করা হয়েছে X এবং Y data দিয়ে
# # model.fit(x,y) 

# # hours = float(input(" Enter how many hours  you study daily : "))

# # #([[value]]) 2d array এর মধ্যে value বসানো হয়েছে, যেখানে value হলো তোমার input data যেমন study_hours এর value।  
# # # // model.predict() method দিয়ে prediction করা হয়েছে, যেখানে value হলো তোমার input data যেমন study_hours এর value। 
# # predicted_marks = model.predict([[hours]]) 



# # print(f"Predicted marks for {hours} hours of study: {predicted_marks[0]:.2f}")


# # Linear Regression self-calculation with any dataset

# from sklearn.linear_model import LinearRegression

# # ১️⃣ Dataset (change this as you like)
# X = [[2], [3], [4], [5], [6]]  # study hours
# Y = [50, 60, 70, 80, 90]       # marks

# # ২️⃣ Model তৈরি
# model = LinearRegression()
# model.fit(X, Y)

# # ৩️⃣ Slope (m) এবং Intercept (c) বের করা
# slope = model.coef_[0]        # m
# intercept = model.intercept_  # c

# print(f"Slope (m) = {slope}")
# print(f"Intercept (c) = {intercept}")

# # ৪️⃣ Prediction (যে কোনো hours এর জন্য)
# hours = float(input("Enter hours you study: "))
# predicted_marks = model.predict([[hours]])
# print(f"Predicted marks for {hours} hours = {predicted_marks[0]:.2f}")




import time
import sys
import random  
# what i lean today linier regation of data  and machine learning and how  to protected your data from hackers and how to make  a  realstic data on based by regretional poiny




def type_text(text, speed=0.01):
    """Print text like it is being typed"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def hacker_line(line_number):

    actions = [
        "Scanning ports", "Accessing database", "Bypassing firewall",
        "Injecting payload", "Decrypting files", "Uploading virus",
        "Connecting to server", "Downloading data", "Initializing protocol",
        "Exploiting vulnerability", "Establishing backdoor", "Harvesting credentials",
        "performing DDos attack", "Bruteforcing password","and covering acteional data in point of regretional data"
    ]
    targets = ["192.168.1.1", "10.0.0.23", "172.16.4.5", "remote_host", "localhost"]
    line = f"[{line_number:03}] {random.choice(actions)} on {random.choice(targets)}..."
    return line


for i in range(1, 101):
    line = hacker_line(i)
    type_text(line, speed=random.uniform(0.005, 0.02))  # random speed for realism
    time.sleep(random.uniform(0.01, 0.05))  # small delay between lines