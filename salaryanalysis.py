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
