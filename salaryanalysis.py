import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Employe_Performance_dataset.csv")
print(data.head())

print("Initial Missing Values:\n")
print(data.isnull().sum())

#Drop rows with missing values
data.dropna(subset=['Performance Score', 'Joining Date'], inplace=True)

#Re-check for Missing Values Post-Cleaning
print("\nMissing Values After Cleaning:\n")
print(data.isnull().sum())

#Code bar chart for age distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20)
plt.title('Age Distribution of Employees (Cleaned Data)')
plt.show()