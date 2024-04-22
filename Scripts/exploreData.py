import pandas as pd

def load_data(file_path, parse_dates=[]):
    """Load the CSV file into a DataFrame."""
    return pd.read_csv(file_path, parse_dates=parse_dates)

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
    enrollments = load_data(enrollments_path, parse_dates=['join_date', 'cancel_date'])
    engagement = load_data(engagement_path, parse_dates=['utc_date'])
    submissions = load_data(submissions_path, parse_dates=['creation_date', 'completion_date'])

    # Explore the data
    print("Enrollments:")
    explore_data(enrollments)

    print("Engagement:")
    explore_data(engagement)

    print("Submissions:")
    explore_data(submissions)

if __name__ == "__main__":
    main()
