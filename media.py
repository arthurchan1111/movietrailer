import webbrowser


class Movie():
    #__init__ is the constructor that creates the instances of a class into memory
    # with unique attribute values of the movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # function to display youtube trailer
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
