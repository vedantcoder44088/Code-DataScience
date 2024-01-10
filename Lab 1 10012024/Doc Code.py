import numpy as np
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
std_deviation = np.std(arr)

print("Array:", arr)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Perform operations on the DataFrame
mean_age = df['Age'].mean()
filtered_data = df[df['Age'] > 25]

print("DataFrame:")
print(df)
print("\nMean Age:", mean_age)
print("\nFiltered Data:")
print(filtered_data)


import matplotlib.pyplot as plt

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

