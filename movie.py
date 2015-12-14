import webbrowser

class Movie:
	"""
	A movie class to store and show basic movie information. 
	"""

	def __init__(self, title, storyline=None, post_image_url=None, trailer_url=None):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = post_image_url
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		"""
		Show movie trailer.
		"""
		webbrowser.open(self.trailer_url)
