import scraper
import helpers
import calculator
import time
import datetime
import os
import pandas as pd
from movie import Movie
import urllib2

movie_id = 'tt0822832'

# Scraping
file_name = scraper.Scrape(movie_id)
# file_name = os.path.join(os.getcwd(), "data", "{0}_movies.csv".format(movie_id))

# Writing
print "\nStarted at",datetime.datetime.now()

columns = ['rating', 'family', 'certification', 'fantasy', 'writers_summary', 'year', 'id', 'biography', 'votes', 'directors_summary', 'cast_summary', 'title', 'sci_fi', 'crime', 'romance', 'animation', 'music', 'comedy', 'type', 'war', 'horror', 'adventure', 'freq', 'thriller', 'mystery', 'creators', 'drama', 'history', 'action', 'runtime', 'western']

path = os.path.join(os.getcwd(), "data", "{0}_workfile.tsv".format(movie_id))
f = open(path, 'w')
f.write('\t'.join(x for x in columns) + '\n')

df = pd.read_csv(file_name)
movies = df[df.freq > df.freq.quantile(.75)]

# f = open(path, 'a')
# output_path = os.path.join(os.getcwd(), "data", "{0}_output.csv".format(movie_id))
# output = pd.read_csv(output_path)
# movies = movies[~movies.title.isin(output.id)]

for index, row in movies.iterrows():
  try:
    movie = Movie(row['title'], row['freq'])
  except (ValueError, urllib2.HTTPError) as e:  # includes simplejson.decoder.JSONDecodeError
    print "\nuyuyorum anlasana"
    time.sleep(5)
    print "anlasana"
    print e
    movie = Movie(row['title'], row['freq'])
    print "uyandim birden seninlee\n"

  f.write('\t'.join(helpers.smart_str(x) for x in movie.__dict__.values()) + '\n')

f.close()
print "Finished at",datetime.datetime.now(),"\n"

# Calculate
calculator.Calculate(movie_id)