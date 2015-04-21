""" Entertainment center module
contains a list of movie instances
"""
from media import Movie
from fresh_tomatoes import open_movies_page

fight_club = Movie('Fight Club',
                    './images/MoviePosterFightClub.jpg',
                    'https://www.youtube.com/watch?v=SUXWAEX2jlg')

moon = Movie('Moon',
             './images/MoviePosterMoon.jpg',
             'https://www.youtube.com/watch?v=twuScTcDP_Q')

space_odyssey = Movie('A Space Odysee',
                      './images/MoviePoster2001.jpg',
                      'https://www.youtube.com/watch?v=XHjIqQBsPjk')

bienvenue_chez_le_chtis = Movie("Bienvenue chez le Ch'tis",
                                "./images/Bienvenue_chez_les_CH'TIS.jpg",
                                "https://www.youtube.com/watch?v=fY5cWL4SUmw")

erleuchtung_garantiert = Movie('Erleuchtung garantiert',
                                './images/ErleuchtungGarantiert.jpg',
                                'https://www.youtube.com/watch?v=lBQyCvxMPyk')

midway = Movie('Midway',
               './images/Midway.jpg',
               'https://www.youtube.com/watch?v=2CGbpbclYyQ')

movies = [ fight_club, moon, space_odyssey,
           bienvenue_chez_le_chtis, erleuchtung_garantiert,
           midway ]
open_movies_page(movies)
