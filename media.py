#  license 
class Movie(object):
	""" This is a Movie class which can create movie instance

	Attributes:
	trailer_youtube_url: The URL of the movie trailer on youtube
	title: The title of this movie
	poster_image_url: The URL of the movie poster 
	"""
	def __init__(self, trailer_youtube_url, title, poster_image_url):
		"""This is a construction fuction which can create an instance of movie class 
		"""
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url
		self.title = title