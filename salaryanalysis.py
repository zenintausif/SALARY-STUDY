#Importing appropriate libaries for visualisations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading in data set and presenting the first few rows
data = pd.read_csv("Employe_Performance_dataset.csv")
print(data.head())

#Presenting values where data is missing
print("Initial Missing Values:")
print(data.isnull().sum())

#Dropping rows with missing values
data.dropna(subset=['Performance Score', 'Joining Date'], inplace=True)

#Re-check for Missing Values Post-Cleaning
print("Missing Values After Cleaning:")
print(data.isnull().sum())

#Code bar chart for age distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, color='skyblue', edgecolor='black') #Colour and edge colour changes to make it more aesthetically pleasing
plt.title('Age Distribution of Employees (Cleaned Data)', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) #Once again, aesthetic adjustments have been made for linestyle
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

#Salary by experience
plt.figure(figsize=(12, 7))
sns.boxplot(x='Experience', y='Salary', data=data, palette='pastel', width=0.6, boxprops={'linewidth': 2}, medianprops={'color': 'darkorange', 'linewidth': 2})
plt.title('Salary by Experience', fontsize=16, fontweight='bold')
plt.xlabel('Years of Experience', fontsize=13)
plt.ylabel('Salary (£)', fontsize=13)
plt.xticks(rotation=45, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

#Salary by gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Salary', data=data, palette='Set2', width=0.6, boxprops={'linewidth': 2}, medianprops={'color': 'crimson', 'linewidth': 2})
plt.title('Salary by Gender (Cleaned Data)', fontsize=14, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Salary (£)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.show()