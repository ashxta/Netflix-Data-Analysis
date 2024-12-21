import pandas as pd

file_path = r"C:\Users\eesho\Downloads\archive\netflix_titles.csv"
netflix_df = pd.read_csv(file_path)

print("Missing values before cleaning:")
print(netflix_df.isnull().sum())

netflix_df = netflix_df.fillna({
    'director': 'Unknown',
    'country': 'Unknown',
    'cast': 'Unknown',
    'rating': 'Not Rated',
    'duration': 'Unknown'
})

print("Missing values after filling:")
print(netflix_df[['director', 'country', 'rating', 'duration']].isnull().sum())

string_columns = ['title', 'director', 'country', 'rating', 'listed_in', 'description']
netflix_df[string_columns] = netflix_df[string_columns].apply(lambda x: x.str.strip())

duplicates = netflix_df.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")

netflix_df = netflix_df.drop_duplicates()

netflix_df['listed_in'] = netflix_df['listed_in'].fillna('')
netflix_genres = netflix_df.assign(genre=netflix_df['listed_in'].str.split(',')).explode('genre')
netflix_genres['genre'] = netflix_genres['genre'].str.strip()

netflix_df['rating'] = netflix_df['rating'].replace({'UR': 'Unrated', 'NR': 'Not Rated'})

netflix_df['duration_numeric'] = (
    netflix_df['duration']
    .str.extract('(\d+)')
    .astype(float, errors='ignore')
)

print("Unique ratings after standardization:")
print(netflix_df['rating'].unique())

# Check for invalid release years and print
invalid_release_years = netflix_df[netflix_df['release_year'] < 1900]
print("Entries with invalid release years:")
print(invalid_release_years)

netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')

invalid_dates = netflix_df[netflix_df['date_added'].isna()]
print(f"Number of invalid dates: {invalid_dates.shape[0]}")

netflix_df['date_added'] = netflix_df['date_added'].fillna(pd.to_datetime('1900-01-01'))

netflix_df['date_added'] = netflix_df['date_added'].dt.strftime('%Y-%m-%d')

netflix_df['date_added'] = netflix_df['date_added'].astype(str)


output_path = r"C:\Users\eesho\Downloads\archive\netflix_titles_cleaned.csv"
netflix_df.to_csv(output_path, index=False)

# Print the path of the saved cleaned dataset
print(f"Cleaned dataset saved at: {output_path}")
