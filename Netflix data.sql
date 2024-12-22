use netflix_db;

SELECT type, COUNT(*) AS count
FROM netflix
GROUP BY type;

SELECT TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(listed_in, ',', numbers.n), ',', -1)) AS genre,
       COUNT(*) AS count
FROM netflix
JOIN (
    SELECT 1 AS n UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
) numbers ON CHAR_LENGTH(listed_in) - CHAR_LENGTH(REPLACE(listed_in, ',', '')) >= numbers.n - 1
WHERE listed_in IS NOT NULL AND listed_in != ''
GROUP BY genre
ORDER BY count DESC
LIMIT 10;

SELECT rating, COUNT(*) AS count
FROM netflix
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY count DESC;

SELECT country, COUNT(*) AS count
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY count DESC
LIMIT 10;

SELECT release_year, COUNT(*) AS movie_count
FROM netflix
WHERE type = 'Movie' AND release_year IS NOT NULL
GROUP BY release_year
ORDER BY movie_count DESC;

SELECT director, COUNT(*) AS title_count
FROM netflix
WHERE director IS NOT NULL AND director != ''
GROUP BY director
ORDER BY title_count DESC
LIMIT 5;

SELECT AVG(CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED)) AS avg_movie_duration
FROM netflix
WHERE type = 'Movie' AND duration IS NOT NULL AND duration != '';

SELECT title, CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) AS seasons
FROM netflix
WHERE type = 'TV Show' AND duration IS NOT NULL AND duration != ''
ORDER BY seasons DESC
LIMIT 10;

SELECT title, CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) AS seasons
FROM netflix
WHERE type = 'TV Show' AND duration IS NOT NULL AND duration != ''
ORDER BY seasons ASC
LIMIT 10;
