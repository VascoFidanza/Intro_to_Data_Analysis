import pandas as pd

def load_data(file_path):
    """Load the CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def explore_data(df):
    """Print basic information and head of the DataFrame."""
    print(df.info())
    print(df.head())
    print("\n" + "-" * 40 + "\n")  # Separator between different dataframes

def main():
    # Define file paths
    enrollments_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEnrollments.csv'
    engagement_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEngagement.csv'
    submissions_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedSubmissions.csv'

    # Load the cleaned data
    enrollments = load_data(enrollments_path)
    engagement = load_data(engagement_path)
    submissions = load_data(submissions_path)

    # Explore the data
    print("Enrollments:")
    explore_data(enrollments)

    print("Engagement:")
    explore_data(engagement)

    print("Submissions:")
    explore_data(submissions)

if __name__ == "__main__":
    main()
