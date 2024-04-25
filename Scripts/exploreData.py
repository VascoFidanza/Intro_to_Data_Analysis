import pandas as pd

def load_data(file_path, parse_dates=[]):
    """Load the CSV file into a DataFrame."""
    return pd.read_csv(file_path, parse_dates=parse_dates)

def explore_data(df):
    """Print basic information and head of the DataFrame."""
    print(df.info())
    print(df.head())
    print("\n" + "-" * 40 + "\n")  # Separator between different dataframes

#Investigating the data - Finding the number of rows in each table and find the number of unique students
def investigatingTheData(filename):
    df = pd.read_csv(filename)
    
    #Counting the number of rows in each data frame
    num_rows = len(df)
    print(f"Number of rows: {num_rows}")    

    # Count unique students
    unique_students = df['account_key'].nunique()
    print(f"Number of unique students: {unique_students}")

def main():
    # Define file paths
    cleanedEnrollments = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEnrollments.csv'
    cleanedEngagement = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEngagement.csv'
    cleanedSubmissions = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedSubmissions.csv'

    filesArray = [cleanedEnrollments, cleanedEngagement, cleanedSubmissions]

    # Load the cleaned data
    enrollments = load_data(cleanedEnrollments, parse_dates=['join_date', 'cancel_date'])
    engagement = load_data(cleanedEngagement, parse_dates=['utc_date'])
    submissions = load_data(cleanedSubmissions, parse_dates=['creation_date', 'completion_date'])

    for file in filesArray:
        print("File: " + file)

        #Investigating
        investigatingTheData(file)

        #print("Data cleaning completed and files saved.")
        print("Data Investigated")


if __name__ == "__main__":
    main()
