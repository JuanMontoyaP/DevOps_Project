from multiprocessing import context
from flask import render_template

from app.helpers.movies import get_popular_movies

from . import api

@api.route('/movies')
def movies():
    popular_movies = get_popular_movies()
    
    context = {
        'popular_movies': popular_movies
    }

    return render_template('movies.html', **context)