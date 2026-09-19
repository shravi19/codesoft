# CODSOFT AI INTERNSHIP
# TASK 4: RECOMMENDATION SYSTEM

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 55)
print("          CODSOFT AI INTERNSHIP")
print("             RECOMMENDATION SYSTEM")
print("=" * 55)

# Movie dataset
data = {
    "title": [
        "Avengers",
        "Iron Man",
        "Spider-Man",
        "Batman",
        "Superman",
        "Interstellar",
        "Inception",
        "Titanic",
        "The Notebook",
        "Jurassic Park"
    ],

    "genre": [
        "action superhero adventure",
        "action superhero science fiction",
        "action superhero adventure",
        "action superhero crime",
        "action superhero science fiction",
        "science fiction adventure space",
        "science fiction thriller",
        "romance drama",
        "romance drama",
        "science fiction adventure"
    ]
}

movies = pd.DataFrame(data)

# Convert movie genres into numerical features
vectorizer = TfidfVectorizer()

genre_matrix = vectorizer.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)


def recommend_movies(movie_name, number=5):

    movie_name = movie_name.lower()

    matching_movies = movies[
        movies["title"].str.lower() == movie_name
    ]

    if matching_movies.empty:
        print("\nMovie not found.")
        print("Please choose a movie from the list.")
        return

    movie_index = matching_movies.index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")
    print("-" * 30)

    count = 0

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        print(
            movies.iloc[index]["title"],
            " - Similarity:",
            round(score, 2)
        )

        count += 1

        if count == number:
            break


# Display available movies
print("\nAvailable Movies:")
for movie in movies["title"]:
    print("-", movie)

# Get user input
movie_name = input(
    "\nEnter a movie you like: "
)

recommend_movies(movie_name)