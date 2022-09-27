import os
from dotenv import load_dotenv
import requests

load_dotenv()

base_url = "https://api.themoviedb.org/3/"
access_api = f'?api_key={os.getenv("API_KEY")}'

def get_movies_from_api():
    api_url = f'{base_url}movie/popular{access_api}'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return []

def get_popular_movies():
    
    api_movies = get_movies_from_api()

    movie_titles = [{"title": movie["title"], "vote_average": movie["vote_average"]} for movie in api_movies]

    return movie_titles
