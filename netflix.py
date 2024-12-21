import pandas as pd

# Load the dataset
file_path = r"C:\Users\eesho\Downloads\archive\netflix_titles.csv"
netflix_df = pd.read_csv(file_path)

# Check for missing values in key columns
print("Missing values before cleaning:")
print(netflix_df.isnull().sum())

# Fill missing values (excluding 'date_added')
netflix_df = netflix_df.fillna({
    'director': 'Unknown',
    'country': 'Unknown',
    'cast': 'Unknown',
    'rating': 'Not Rated',
    'duration': 'Unknown'
})

# Verify changes
print("Missing values after filling:")
print(netflix_df[['director', 'country', 'rating', 'duration']].isnull().sum())

# Strip whitespace from string columns (excluding 'date_added')
string_columns = ['title', 'director', 'country', 'rating', 'listed_in', 'description']
netflix_df[string_columns] = netflix_df[string_columns].apply(lambda x: x.str.strip())

# Find and print duplicate rows
duplicates = netflix_df.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")

# Drop duplicate rows
netflix_df = netflix_df.drop_duplicates()

# Explode genres into separate rows
netflix_df['listed_in'] = netflix_df['listed_in'].fillna('')
netflix_genres = netflix_df.assign(genre=netflix_df['listed_in'].str.split(',')).explode('genre')
netflix_genres['genre'] = netflix_genres['genre'].str.strip()

# Standardize and replace inconsistent or null ratings
netflix_df['rating'] = netflix_df['rating'].replace({'UR': 'Unrated', 'NR': 'Not Rated'})

# Extract numeric part of duration, handling unknown values
netflix_df['duration_numeric'] = (
    netflix_df['duration']
    .str.extract('(\d+)')
    .astype(float, errors='ignore')
)

# Verify unique ratings
print("Unique ratings after standardization:")
print(netflix_df['rating'].unique())

# Check for invalid release years and print
invalid_release_years = netflix_df[netflix_df['release_year'] < 1900]
print("Entries with invalid release years:")
print(invalid_release_years)

# Convert 'date_added' from string format (e.g., 'September 21, 2021') to datetime format
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')

# Check for invalid 'date_added' (NaT values) and handle them
invalid_dates = netflix_df[netflix_df['date_added'].isna()]
print(f"Number of invalid dates: {invalid_dates.shape[0]}")

# Replace invalid dates with a default value (e.g., '1900-01-01') or any value you prefer
netflix_df['date_added'] = netflix_df['date_added'].fillna(pd.to_datetime('1900-01-01'))

# Format 'date_added' to the desired string format (YYYY-MM-DD)
netflix_df['date_added'] = netflix_df['date_added'].dt.strftime('%Y-%m-%d')

# Ensure the 'date_added' column is treated as text for saving as CSV
netflix_df['date_added'] = netflix_df['date_added'].astype(str)

# Save the cleaned dataset
output_path = r"C:\Users\eesho\Downloads\archive\netflix_titles_cleaned.csv"
netflix_df.to_csv(output_path, index=False)

# Print the path of the saved cleaned dataset
print(f"Cleaned dataset saved at: {output_path}")
