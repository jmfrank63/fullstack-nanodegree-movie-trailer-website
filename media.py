"""Media module containing the movie class
"""


class Movie(object):
    """A simple movie class containing the title the  """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """init instance variables """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def __str__(self):
        """Print a representation of the class """
        return ''.join(['Title: ', self.title, '\nImage: ',
                        self.poster_image_url,
                        '\nTrailer: ', self.trailer_youtube_url])
