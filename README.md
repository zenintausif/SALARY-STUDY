# What factors affect salary?
DAT5902 Final Project

## **Overview**
This project analyses the factors influencing salary distribution within an organisation, focusing on internal variables such as performance, experience, and gender. Using Python for data exploration and visualisation, the findings highlight trends and disparities to provide actionable insights into compensation structures.

## **Repository Structure**
The repository contains the following files and folders:

- **`.circleci/`**: Configuration files for continuous integration using CircleCI, ensuring code quality and test automation.  
- **`tests/`**: Contains unit tests to validate the data cleaning and visualisation functions.  
- **`.gitignore`**: Specifies files and directories to be ignored by Git.  
- **`Employe_Performance_dataset.csv`**: The original dataset used for the analysis.  
- **`README.md`**: Provides an overview of the project and instructions for usage.  
- **`requirements.txt`**: Lists all Python dependencies required to run the project.  
- **`salaryanalysis.py`**: The main Python script containing the data cleaning, analysis, and visualisation code.

## **Dataset**
- **Source**: The dataset was sourced from Kaggle.  
- **Description**: Includes 1,000 entries and 12 columns detailing employee attributes such as age, gender, department, salary, performance score, and experience.  
- **Preprocessing**: Missing performance scores (498 entries) were dropped, and duplicate checks ensured data consistency.

## **Setup Instructions**
1. Clone the repository:  
   ```bash
   git clone https://github.com/zenintausif/salary-study.git
   cd salary-study
   ```

2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis script:  
   ```bash
   python salaryanalysis.py
   ```

4. Run unit tests:  
   ```bash
   pytest tests/
   ```
