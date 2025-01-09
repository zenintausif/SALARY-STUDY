import pandas as pd

#Load in dataset
data = pd.read_csv('Employe_Performance_dataset.csv')

def test_no_nulls():
    
    # Test that no null values exist in the dataset
    assert data.isnull().sum().sum() == 0, "Null values are present in the dataset."