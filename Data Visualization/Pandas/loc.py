# loc কী?

# English:
# loc is used to access and modify data in Pandas DataFrame by label/index.

# বাংলায়:
# loc দিয়ে আমরা DataFrame এর নির্দিষ্ট row, column খুঁজে বের করে update করতে পারি।

# 🔹 Example Dataset
import pandas as pd

data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Anisa", "Kawser", "Rafi", "Sumi"],
    "Score": [85, 90, 75, 88]
}

df = pd.DataFrame(data)
print(df)

# 
# ✅ Output:

#    ID    Name  Score
# 0   1   Anisa     85
# 1   2  Kawser     90
# 2   3    Rafi     75
# 3   4    Sumi     88

# 🔹 Updating Data using loc
# 1. Update single value
# Update Rafi's Score → 95
df.loc[df["Name"] == "Rafi", "Score"] = 95
print(df)


# ✅ Output:

#    ID    Name  Score
# 0   1   Anisa     85
# 1   2  Kawser     90
# 2   3    Rafi     95
# 3   4    Sumi     88

# 2. Update multiple columns in a row
# Update Sumi's Name and Score
df.loc[df["ID"] == 4, ["Name", "Score"]] = ["Sumaiya", 92]
print(df)


# ✅ Output:

#    ID     Name  Score
# 0   1    Anisa     85
# 1   2   Kawser     90
# 2   3     Rafi     95
# 3   4  Sumaiya     92

# 3. Conditional Update
# Increase all Score by 5 where Score < 90
df.loc[df["Score"] < 90, "Score"] = df["Score"] + 5
print(df)


# 👉 এখানে শুধু যাদের Score 90 এর নিচে, তাদের স্কোর ৫ বাড়বে।

# 4. Update entire column
# Add 10 bonus to all Score
df.loc[:, "Score"] = df["Score"] + 10
print(df)

# 🔹 Summary (Bangla + English)

# df.loc[row_condition, "Column"] = new_value → single update

# df.loc[row_condition, ["Col1", "Col2"]] = [val1, val2] → multiple update

# df.loc[:, "Column"] = ... → পুরো column update

# 👉 চাইলে আমি তোমাকে Practice Tasks বানিয়ে দিতে পারি (যেমন "90 এর নিচে নামকে 'Failed' set করা", "ID odd হলে score +3 করা") — এগুলো করলে loc একদম মাস্টারি হয়ে যাবে।

# চাও কি আমি সেই Practice Task List বানিয়ে দিই?

# You said:
# dew
# ChatGPT said:

# ঠিক আছে ভাই 😃 এখন তোমার জন্য Pandas loc দিয়ে Data Update করার Practice Tasks বানিয়ে দিলাম।

# 📝 Practice Tasks: Updating Data using loc
# ✅ Task 1: Single Value Update

# একটা DataFrame বানাও, যেখানে ID, Name, Score থাকবে।
# 👉 loc দিয়ে ৩rd student-এর Score = 100 করে দাও।

# ✅ Task 2: Multiple Column Update

# 👉 ID == 2 হলে Name = "Updated" আর Score = 80 set করো।

# ✅ Task 3: Conditional Update

# 👉 যাদের Score < 90, তাদের Score + 5 করো।

# ✅ Task 4: Update Based on Multiple Conditions

# 👉 যাদের Score > 95 AND Name starts with "A", তাদের Score = 99 করে দাও।

# ✅ Task 5: Update Entire Column

# 👉 সব Student এর Score-এ 10 bonus যোগ করো।

# ✅ Task 6: Replace Failed Students

# 👉 যাদের Score < 60, তাদের Name column-এ "Failed" লিখে দাও।

# ✅ Task 7: Bulk Update with loc

# 👉 ID odd হলে Score + 3, আর ID even হলে Score + 7 করে দাও।

# 🔹 Example Starter Code


import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Anisa", "Kawser", "Rafi", "Sumi", "Nila"],
    "Score": [85, 90, 75, 55, 99]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 👉 এখানে তোমার Practice Task গুলো



