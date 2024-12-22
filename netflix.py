import pandas as pd

# Load the dataset
file_path = r"C:\Users\eesho\Downloads\archive\netflix_titles.csv"
netflix_df = pd.read_csv(file_path)

#Handle Missing Values
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

#Strip Whitespaces
string_columns = ['title', 'director', 'country', 'rating', 'listed_in', 'description']
netflix_df[string_columns] = netflix_df[string_columns].apply(lambda x: x.str.strip())

#Remove Duplicates
duplicates = netflix_df.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")
netflix_df = netflix_df.drop_duplicates()

# Standardize Rating Values
netflix_df['rating'] = netflix_df['rating'].replace({'UR': 'Unrated', 'NR': 'Not Rated'})

netflix_df['duration_numeric'] = (
    netflix_df['duration']
    .str.extract('(\d+)')
    .astype(float, errors='ignore')
)

#Validate Release Year
invalid_release_years = netflix_df[netflix_df['release_year'] < 1900]
print("Entries with invalid release years:")
print(invalid_release_years)

#Clean Date Added Column
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce', dayfirst=True)
invalid_dates = netflix_df[netflix_df['date_added'].isna()]
print(f"Number of invalid dates: {invalid_dates.shape[0]}")
netflix_df['date_added'] = netflix_df['date_added'].fillna(pd.to_datetime('1900-01-01'))
netflix_df['date_added'] = netflix_df['date_added'].dt.strftime('%Y-%m-%d')

netflix_df['listed_in'] = netflix_df['listed_in'].fillna('')
netflix_genres = netflix_df.assign(genre=netflix_df['listed_in'].str.split(',')).explode('genre')
netflix_genres['genre'] = netflix_genres['genre'].str.strip()

#Save Cleaned Dataset
output_path = r"C:\Users\eesho\Downloads\archive\netflix_titles_cleaned.csv"
netflix_df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved at: {output_path}")
