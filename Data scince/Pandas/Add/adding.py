import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        "Salary": [50000, 60000, 70000]


         }

df = pd.DataFrame(data)

print('Before adding new column:');
print(df);


# Adding a new column 'bonus' to the DataFrame

df['bonus'] =df['Salary'] * 0.10 # adding a new column 'bonus' to the DataFrame by multiplying the 'Salary' column by 0.10  

print('After adding new column:');
print(df);

#Using the INSERT() method to add a new column to the DataFrame

df.insert(2, 'Country', ['USA', 'Canada', 'Mexico'])


# df.insert(loc, column, value, allow_duplicates=False



print('After using INSERT() method:');



df.insert(0,"ID",[1,2,3,])
print(df);

