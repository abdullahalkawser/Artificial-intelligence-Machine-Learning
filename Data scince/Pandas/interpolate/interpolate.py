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