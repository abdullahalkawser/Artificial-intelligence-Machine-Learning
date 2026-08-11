import pandas as pd 
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)
print("Original DataFrame:") # original DataFrame is printed to the console
print(df)


print(df)
# df.to_csv("data.csv", index=False)

df.to_excel("data.xlsx", index=False) #create an excel file

df.to_json("data.json", orient="records") #create a json file
