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
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Employees (Cleaned Data)', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()


#Code bar chart for salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Salary'], bins=30, color='mediumseagreen', edgecolor='black')
plt.title('Salary Distribution (Cleaned Data)', fontsize=14, fontweight='bold')
plt.xlabel('Salary (£)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

#Salary by performance score 
plt.figure(figsize=(10, 6))
sns.boxplot(x='Performance Score', y='Salary', data=data, palette='muted', width=0.6, boxprops={'linewidth': 2}, medianprops={'color': 'firebrick', 'linewidth': 2})
plt.title('Salary by Performance Score', fontsize=14, fontweight='bold')
plt.xlabel('Performance Score', fontsize=12)
plt.ylabel('Salary (£)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()