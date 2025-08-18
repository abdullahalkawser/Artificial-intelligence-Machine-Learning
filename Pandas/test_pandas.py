import pandas as pd

# একটি সিম্পল ডেটা তৈরি করি
data = {
    "Name": ["Anu", "Rahim", "Kawser"],
    "Age": [22, 25, 21],
    "City": ["Dhaka", "Chittagong", "Khulna"]
}

# DataFrame তৈরি
df = pd.DataFrame(data)

# পুরো DataFrame দেখাও
print("Complete DataFrame:")
print(df)

# শুধু নামের কলাম দেখাও
print("\nName Column:")
print(df["Name"])

# বয়স 22 এর বেশি যাদের দেখাও
print("\nAge > 22:")
print(df[df["Age"] > 22])
