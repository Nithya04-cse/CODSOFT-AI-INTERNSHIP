movies = {
    "Action": ["Avengers", "Batman", "Iron Man"],
    "Comedy": ["Jumanji", "The Mask", "Home Alone"],
    "Drama": ["Titanic", "Forrest Gump", "The Pursuit of Happyness"],
    "Sci-Fi": ["Interstellar", "Inception", "Matrix"]
}

print("Movie Recommendation System")
print("Available genres:", ", ".join(movies.keys()))

genre = input("Enter a genre: ").title()

if genre in movies:
    print("Recommended movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Sorry, genre not found.")
