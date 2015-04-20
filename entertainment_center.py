""" Entertainment center module
contains a list of movie instances
"""
from media import Movie
from fresh_tomatoes import open_movies_page

fight_club = Movie('Fight Club',
                    'http://api.ning.com/files/eUrPno3TQ7XYJ6AOpoykz2Sm2aeanh6xyLLwFqB1bd*dvpJ2k5rh36TNt2DRjSE1SiNT*GnD5mtDP1bqHlJvesfbdfzlWG7Q/MoviePosterFightClub.jpg',
                    'https://www.youtube.com/watch?v=SUXWAEX2jlg')

movies = [ fight_club ]
open_movies_page(movies)
