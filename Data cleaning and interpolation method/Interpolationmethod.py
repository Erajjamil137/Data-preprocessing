import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Eraj', 'Taha', 'Hunniyah', 'Abdullah', 'Awais', 'Aleezza', 'Bunty', 'Ali'] ,
    'Age' : [22, 24, np.nan, 23, 25, 21, np.nan, 26] ,
    'Salary' : [45000, 52000, 58000, np.nan, 50000, np.nan, 49000, 60000] ,
    'Category' : ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}

# Creating a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame with Missing Values:")
print(df)

# Interpolating numerical columns(Age and Salary)
df['Age'] = df['Age'].interpolate(method = 'linear')
df['Salary'] = df['Salary'].interpolate(method = 'linear')

print("\nDataFrame after Interpolation:")
print(df)
