"""Ultra simple test file for the media module"""
import media

# create a movie instance and test its __str__ method
midway = media.Movie('Midway',
                     './images/Midway.jpg',
                     'https://www.youtube.com/watch?v=2CGbpbclYyQ')

print(midway)
