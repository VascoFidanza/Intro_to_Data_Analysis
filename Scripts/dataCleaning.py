import pandas as pd
import numpy as np

# Function to clean enrollment data
def clean_enrollments(filename):
    df = pd.read_csv(filename)
    
    df['days_to_cancel'] = pd.to_numeric(df['days_to_cancel'], errors='coerce').fillna(0).astype(int)
    df['cancel_date'] = pd.to_datetime(df['cancel_date'], errors='coerce')
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce', format='%Y-%m-%d')

    # Replace 'cleaned_enrollments.csv' with the path/filename you want to save to
    df.to_csv('/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEnrollments.csv', index=False)

# Function to clean engagement data
def clean_engagement(filename):
    df = pd.read_csv(filename)
    
    df['utc_date'] = pd.to_datetime(df['utc_date'], errors='coerce', format='%Y-%m-%d')
    df['num_courses_visited'] = pd.to_numeric(df['num_courses_visited'], errors='coerce').fillna(0).astype(int)
    df['lessons_completed'] = pd.to_numeric(df['lessons_completed'], errors='coerce').fillna(0).astype(int)
    df['projects_completed'] = pd.to_numeric(df['projects_completed'], errors='coerce').fillna(0).astype(int)
    df['total_minutes_visited'] = pd.to_numeric(df['total_minutes_visited'], errors='coerce').fillna(0).astype(float)
    
    # Replace 'cleaned_engagement.csv' with the path/filename you want to save to
    df.to_csv('/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedEngagement.csv', index=False)

# Function to clean submissions data
def clean_submissions(filename):
    df = pd.read_csv(filename)
    
    df['creation_date'] = pd.to_datetime(df['creation_date'], errors='coerce', format='%Y-%m-%d')
    df['completion_date'] = pd.to_datetime(df['completion_date'], errors='coerce', format='%Y-%m-%d')
    df['account_key'] = pd.to_numeric(df['account_key'], errors='coerce').fillna(0).astype(int)
    df['lesson_key'] = pd.to_numeric(df['lesson_key'], errors='coerce').fillna(0).astype(int)
    
    # Replace 'cleaned_submissions.csv' with the path/filename you want to save to
    df.to_csv('/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/cleanedSubmissions.csv', index=False)

def main():
    # Define file paths
    enrollments_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/enrollments.csv'
    engagement_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/daily_engagement.csv'
    submissions_path = '/Users/vascofidanza/Documents/Data Analytics Projects/Udacity/Intro_to_Data_Analysis/Data/project_submissions.csv'

    # Clean data
    clean_enrollments(enrollments_path)
    clean_engagement(engagement_path)
    clean_submissions(submissions_path)

    print("Data cleaning completed and files saved.")

if __name__ == "__main__":
    main()
