from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)


# TMDb API URL and key
tmdb_api_url = "https://api.themoviedb.org/3"
tmdb_api_key = "1f30c307ae04cc9fcf64fae25743745d" 

# Function to fetch genre IDs
def fetch_genre_ids():
    genres_url = f"{tmdb_api_url}/genre/movie/list"
    params = {"api_key": tmdb_api_key}
    response = requests.get(genres_url, params=params)
    genre_data = response.json().get("genres", [])
    return {genre["name"].lower(): genre["id"] for genre in genre_data}

# Function to fetch movies by genre
def get_movies_by_genre(genre_id):
    discover_url = f"{tmdb_api_url}/discover/movie"
    params = {
        "api_key": tmdb_api_key,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(discover_url, params=params)
    return response.json().get("results", [])

# Function to get poster URL for a movie
def get_movie_poster(movie_id):
    movie_url = f"{tmdb_api_url}/movie/{movie_id}"
    params = {"api_key": tmdb_api_key}
    response = requests.get(movie_url, params=params)
    poster_path = response.json().get("poster_path")
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return None

# Function to get user input for favorite genre
def get_user_input():
    return request.form.get('genre').lower()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fav_genre_name = get_user_input()

        # Fetch genre IDs
        genre_ids = fetch_genre_ids()

        # Check if the input genre is valid
        if fav_genre_name in genre_ids:
            # Fetch a list of movies in the favorite genre
            movies = get_movies_by_genre(genre_ids[fav_genre_name])

            # Select a random movie
            if movies:
                recommended_movie = random.choice(movies)
                poster_url = get_movie_poster(recommended_movie['id'])
                return render_template('index.html', movie=recommended_movie, poster_url=poster_url)
            else:
                return render_template('index.html', message="No movies found in your favorite genre.")
        else:
            return render_template('index.html', message="Invalid genre. Please enter a valid genre name.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
