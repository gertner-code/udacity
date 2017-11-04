import webbrowser


class Movie():
    """This class stores movie related information and open movie trailers."""

    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        # initializes instanced variables
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # opens youtube trailer in browser
        webbrowser.open(self.trailer_youtube_url)
