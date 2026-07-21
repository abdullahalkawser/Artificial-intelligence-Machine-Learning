# model tarin practice for linear regression with any datasets
from sklearn.linear_model import LinearRegression;
# ১️⃣ Dataset (change this as you like)
X = [[2], [3], [4], [5], [6]]  # hours of study in 2d array like [[2], [3], [4], [5], [6]]
Y = [50, 60, 70, 80, 90]       # marks
#model তৈরি
model = LinearRegression()

#model train করা
model.fit(X, Y)
# Slope (m) এবং Intercept (c) বের করা
slope = model.coef_[0]        # m
intercept = model.intercept_  # c
print(f"Slope (m) = {slope}")
print(f"Intercept (c) = {intercept}")
# Prediction (যে কোনো hours এর জন্য)
hours = float(input("Enter hours you study: "))
predicted_mark = model.predict([[hours]])
print(f"Predicted mark for {hours} hours of study: {predicted_mark[0]}")


