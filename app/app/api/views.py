from . import api

@api.route('/movies')
def get_all_movies():
    return "Movies"