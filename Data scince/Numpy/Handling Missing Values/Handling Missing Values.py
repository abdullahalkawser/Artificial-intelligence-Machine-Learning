# import pandas as pd
# import numpy as np

# data = pd.DataFrame({
#     "Name": ["Rahim", "Karim", "Sakib"],
#     "Age": [22, np.nan, 24],
#     "Salary": [25000, 30000, np.nan]
# })

# print(data.isnull().sum())

import numpy as np

a = np.array([10, 20, np.nan, 40, 50, np.nan, 70, 80, 90, np.nan])

# print(np.isnan(a))

a = np.nan_to_num(a, nan=1000)
print(a)


import numpy as np

# Array with missing value (NaN)
marks = np.array([70, 80, np.nan, 90, 60])

print("Original Data:")
print(marks)

# 1. Check which values are NaN
print("\nNaN Check:")
print(np.isnan(marks))

# 2. Mean - NaN বাদ দিয়ে Average
print("\nMean:")
print(np.nanmean(marks))

# 3. Median - NaN বাদ দিয়ে Median
print("\nMedian:")
print(np.nanmedian(marks))

# 4. Sum - NaN বাদ দিয়ে Total
print("\nSum:")
print(np.nansum(marks))

# 5. Maximum - NaN বাদ দিয়ে Highest
print("\nMaximum:")
print(np.nanmax(marks))

# 6. Minimum - NaN বাদ দিয়ে Lowest
print("\nMinimum:")
print(np.nanmin(marks))