"""A class containing information about the movies"""
import webbrowser


class Movie(object):
    """Blueprint for the object of type movies.
    Attributes:
        title: The movie's title.
        storyline: One line story of the movie.
        poster_image_url: URL of movie's poster.
        trailer_youtube_url: URL of movie's poster
    """

    def __init__(self, movie_title, movie_story, poster_image,
                 trailer_youtube):
        """Initilizaling instance variables"""
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Play trailer in browser"""
        webbrowser.open(self.trailer_youtube_url)
