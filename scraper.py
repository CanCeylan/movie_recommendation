import time
import datetime
from lxml import html
import requests
from operator import itemgetter
import pandas as pd
import os

def get_lists(movie_id):

  lists_url = "http://www.imdb.com/lists/%s" % movie_id

  page = requests.get(lists_url)
  tree = html.fromstring(page.content)
  lists = tree.xpath('//div[@class="list_name"]/b//a')

  return [l.attrib['href'][6:-1] for l in lists]

def get_movies(list_id):

  list_url = "http://www.imdb.com/list/%s" % list_id
  # print "Getting all movies in the list %s" % list_id

  page = requests.get(list_url)
  tree = html.fromstring(page.content)
  movies = tree.xpath('//div[@class="info"]/b//a')

  return [m.attrib['href'][7:-1] for m in movies]

def add_movies(all_movies, movies):

  for movie in movies:
    if movie in all_movies:
      all_movies[movie] += 1
    else:
      all_movies[movie] = 1

  return all_movies

def get_all_movies(lists):

  all_movies = {}

  for list in lists:
    movies = get_movies(list)
    all_movies = add_movies(all_movies, movies)
    time.sleep(1)

  df = pd.DataFrame.from_dict(all_movies, orient='index').reset_index()
  df.rename(columns={'index': 'title', 0: 'freq'}, inplace=True)
  return df

def Scrape(movie_id):

  print "Started at",datetime.datetime.now()
  path = os.path.join(os.getcwd(), "data", "{0}_movies.csv".format(movie_id))
  lists = get_lists(movie_id)
  recs = get_all_movies(lists)
  recs.to_csv(path)
  print "Finished at",datetime.datetime.now()

  return path


# Scrape('tt1727776')

