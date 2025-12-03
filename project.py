import pandas as pd
import numpy as np

# Create a dictionary with the provided values, using np.nan for nulls
data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', np.nan, np.nan, np.nan],
    'Salary': [100, 200, np.nan, np.nan]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)
