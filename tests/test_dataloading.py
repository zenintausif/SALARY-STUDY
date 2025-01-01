import os
import pandas as pd

def test_file_found():
    #Testing to see if the data file exists
    assert os.path.exists('Employe_Performance_dataset.csv'), "Error! Data set file is missing."

def test_file_read():
    #Testing to see if the dataset can be read without errors
    data = pd.read_csv('Employe_Performance_dataset.csv')
    assert data is not None, "Error! Dataset could not be read."

def test_data_empty():
    #testing to see that the dataset is not empty
    data = pd.read_csv('Employe_Performance_dataset.csv')
    assert len(data) > 0, "Error! Dataset is empty."



