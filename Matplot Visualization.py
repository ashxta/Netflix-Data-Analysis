import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\netflix_titles_cleaned.csv"
netflix_df = pd.read_csv(file_path)

# Set the plot style
sns.set(style="whitegrid")

# Count of content type
content_type = netflix_df['type'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=content_type.index, y=content_type.values, palette="viridis", errorbar=None, hue=content_type.index, dodge=False)
plt.title("Count of Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.legend([], [], frameon=False) 
plt.show()

# Top 10 Genres
netflix_df['listed_in'] = netflix_df['listed_in'].fillna('')
top_genres = netflix_df['listed_in'].str.split(',').explode().str.strip().value_counts().head(10)
plt.figure(figsize=(10, 8))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="plasma", errorbar=None, hue=top_genres.index, dodge=False)
plt.title("Top 10 Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.legend([], [], frameon=False)
plt.show()

# Distribution of Ratings
ratings = netflix_df['rating'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=ratings.index, y=ratings.values, palette="coolwarm", errorbar=None, hue=ratings.index, dodge=False)
plt.title("Distribution of Ratings")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.legend([], [], frameon=False)
plt.show()

# Content added over time
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')
added_by_year = netflix_df['date_added'].dt.year.value_counts().sort_index()
plt.figure(figsize=(12, 6))
added_by_year.plot(kind='bar', color='skyblue')
plt.title("Content Added Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top 10 Countries producing content
top_countries = netflix_df['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="magma", errorbar=None, hue=top_countries.index, dodge=False)
plt.title("Top 10 Countries Producing Content")
plt.xlabel("Count")
plt.ylabel("Country")
plt.legend([], [], frameon=False)
plt.show()

# Movie Duration Distribution
netflix_df['duration'] = netflix_df['duration'].fillna('0')
movie_duration = netflix_df[netflix_df['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float)
plt.figure(figsize=(12, 6))
plt.hist(movie_duration[0], bins=30, color='purple', edgecolor='black')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")
plt.show()

# Content count by release year
release_year_counts = netflix_df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
release_year_counts.plot(kind='line', color='green', marker='o')
plt.title("Content Count by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# TV Shows Duration Distribution
tv_duration = netflix_df[netflix_df['type'] == 'TV Show']['duration'].str.extract('(\d+)').astype(float)
plt.figure(figsize=(12, 6))
plt.hist(tv_duration[0], bins=20, color='orange', edgecolor='black')
plt.title("Distribution of TV Show Durations (Seasons)")
plt.xlabel("Number of Seasons")
plt.ylabel("Frequency")
plt.show()
