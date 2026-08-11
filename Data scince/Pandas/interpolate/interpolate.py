interpolate() কী?

Pandas-এর interpolate() ব্যবহার করা হয় missing value (NaN) অনুমান করে পূরণ করার জন্য।

সহজভাবে:

আগের ও পরের value দেখে মাঝখানের missing value-এর একটি reasonable value বের করে দেয়।

import pandas as pd

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [30, 32, None, 34, 35]
}

df = pd.DataFrame(data)

print(df)

df["Temperature"] = df["Temperature"].interpolate()

print("\nAfter interpolation:")
print(df)

interpolate() এর প্রধান Methods
df.interpolate(method="linear")
1. linear ⭐⭐⭐⭐⭐

সবচেয়ে common এবং default method।

দুই পাশের value-এর মধ্যে straight-line/সমান হারে missing value বের করে।

data = [10, 20, None, 40]

# Result
10, 20, 30, 40
df.interpolate(method="linear")

কখন?
সাধারণ numeric data বা evenly changing data হলে।

2. polynomial

Polynomial equation ব্যবহার করে missing value estimate করে।

df.interpolate(method="polynomial", order=2)

এখানে:

order=2 → Quadratic
order=3 → Cubic

কখন?
Data যদি straight line না হয়ে curve-এর মতো pattern follow করে।

3. spline

Spline ব্যবহার করে smooth curve তৈরি করে missing value estimate করে।

df.interpolate(method="spline", order=2)

কখন?
Data-তে smooth/curved pattern থাকলে।

4. time

Time-series data-এর জন্য।

df.interpolate(method="time")

এটা ব্যবহার করতে সাধারণত DataFrame-এর index datetime হতে হয়।

Example:

2026-01-01 → 100
2026-01-02 → NaN
2026-01-03 → 140

এখানে date/time-এর ভিত্তিতে interpolation করবে।

5. index

Index-এর numeric value ব্যবহার করে interpolation করে।

df.interpolate(method="index")

যখন index-এর distance সমান নয়, তখন এটি useful হতে পারে।

6. values

DataFrame-এর values-এর index position অনুযায়ী interpolation।

df.interpolate(method="values")

তবে practical Pandas কাজের ক্ষেত্রে linear / time / polynomial / spline বেশি গুরুত্বপূর্ণ।

nterpolate() কখন ব্যবহার করব?

এটা সবচেয়ে important 👇

✅ ব্যবহার করবে যখন:
Data-এর মধ্যে NaN আছে
Missing value-এর আগে ও পরে meaningful numeric value আছে
Data-এর একটা natural sequence আছে
যেমন:
Temperature
Stock price
Sensor data
Time-series data
Sales data
Measurement data





🔥 কোনগুলো আগে শিখবে?

তোমার Data Science + ML learning অনুযায়ী:

Method	Importance	সহজ ভাষায়
linear ⭐⭐⭐⭐⭐	খুব বেশি	Straight line
time ⭐⭐⭐⭐⭐	Time-series	সময় অনুযায়ী
polynomial ⭐⭐⭐⭐	বেশি	Curve/equation
spline ⭐⭐⭐⭐	বেশি	Smooth curve
index ⭐⭐⭐	মাঝারি	Index অনুযায়ী
values ⭐⭐	কম	Value position অনুযায়ী
🧠 Shortcut
Linear       → Straight line
Polynomial   → Mathematical curve
Spline       → Smooth curve
Time         → Date/Time data
Index        → Index অনুযায়ী
Values       → Position/values অনুযায়ী
⚠️ একটা গুরুত্বপূর্ণ বিষয়

সব interpolation method সব Pandas version-এ একইভাবে available নাও থাকতে পারে। বিশেষ করে polynomial ও spline ব্যবহার করলে সাধারণত order দিতে হয় এবং SciPy dependency প্রয়োজন হতে পারে।

Exam/Interview-এর জন্য সবচেয়ে important:
linear, time, polynomial, spline — এই ৪টা আগে ভালোভাবে বুঝে রাখো।