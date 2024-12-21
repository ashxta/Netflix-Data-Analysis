import pandas as pd

# Load the dataset
file_path = r"C:\Users\eesho\Downloads\archive\netflix_titles_cleaned.csv"
netflix_df = pd.read_csv(file_path)

# Try parsing with multiple date formats (coercing errors)
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce', dayfirst=True)

# Print the first few rows to check the result
print(netflix_df[['date_added']].head())

# Save the cleaned dataset back to CSV if successful
output_path = r"C:\Users\eesho\Downloads\archive\netflix_titles_cleaned_fixed.csv"
netflix_df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved at: {output_path}")
