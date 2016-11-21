from imdbpie import Imdb
import urllib2

class Movie:

  def __init__(self, id, freq):

    imdb = Imdb()
    imdb = Imdb(anonymize=True) # to proxy requests

    print id
    try:
      movie = imdb.get_title_by_id(id)
    except urllib2.HTTPError as err:
      print err

    if movie is None:
      print "bu None Abiii"
      print movie

    self.id = id
    self.title = movie.title
    self.freq = freq
    self.year = movie.year
    # self.tagline = movie.tagline
    self.rating = movie.rating
    self.type = movie.type
    self.cast_summary = movie.cast_summary
    self.writers_summary = movie.writers_summary
    self.creators = movie.creators
    self.directors_summary = movie.directors_summary
    self.runtime = movie.runtime
    self.votes = movie.votes
    self.certification = movie.certification
    self.action = 0
    self.comedy = 0
    self.horror = 0
    self.adventure = 0
    self.drama = 0
    self.thriller = 0
    self.romance = 0
    self.sci_fi = 0
    self.western = 0
    self.mystery = 0
    self.history = 0
    self.crime = 0
    self.biography = 0
    self.fantasy = 0
    self.war = 0
    self.family = 0
    self.music = 0

    for g in movie.genres:
      if g.lower() == 'action':
        self.action = 1
      elif g.lower() == 'comedy':
        self.comedy = 1
      elif g.lower() == 'horror':
        self.horror = 1
      elif g.lower() == 'adventure':
        self.adventure = 1
      elif g.lower() == 'drama':
        self.drama = 1
      elif g.lower() == 'thriller':
        self.thriller = 1
      elif g.lower() == 'romance':
        self.romance = 1
      elif g.lower() == 'sci-fi':
        self.sci_fi = 1
      elif g.lower() == 'western':
        self.western = 1
      elif g.lower() == 'mystery':
        self.mystery = 1
      elif g.lower() == 'history':
        self.history = 1
      elif g.lower() == 'crime':
        self.crime = 1
      elif g.lower() == 'biography':
        self.biography = 1
      elif g.lower() == 'fantasy':
        self.fantasy = 1
      elif g.lower() == 'war':
        self.war = 1
      elif g.lower() == 'family':
        self.family = 1
      elif g.lower() == 'music':
        self.music = 1