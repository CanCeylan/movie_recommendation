import pandas as pd
import os

def Calculate(movie_id):

  path = os.path.join(os.getcwd(), "data", "{0}_workfile.tsv".format(movie_id))
  df = pd.read_csv(path, sep='\t')

  columns = ['id', 'title', 'freq', 'rating', 'year', 'votes', 'runtime', 'type', 'certification', 'action', 'comedy', 'horror', 'thriller', 'adventure', 'mystery', 'drama', 'history', 'sci_fi', 'crime', 'romance', 'music', 'western', 'war', 'biography', 'fantasy', 'family']
  df = df[columns]
  df = df.sort_values(by='freq', ascending=False)
  df[['freq','rating','votes','year','runtime']] = df[['freq','rating','votes','year','runtime']].apply(pd.to_numeric, errors='coerce')

  target_movie = df[:1]

  adjusters = ['year','rating','votes','runtime','freq']
  for col in df.columns:
      if col in adjusters:
          target = float(target_movie[col])
          denom = max(abs(df[col]-target))
          df['adj_' + col] = 1-abs(df[col]-target)/denom

  categories = ['action', 'comedy', 'horror', 'thriller', 'adventure', 'mystery', 'drama', 'history', 'sci_fi', 'crime', 'romance', 'music', 'western', 'war', 'biography', 'fantasy', 'family']
  ratios = pd.DataFrame()

  for cat in df.columns:
    if cat in categories:
        df['adj_' + cat] = 1
        ratios[cat] = df[cat].value_counts(normalize=True)

  ratios = ratios.fillna(0)

  for cat in df.columns:
    if cat in categories:
        column_name = str('adj_' + cat)
        if int(target_movie[cat]) == 1:
            df.ix[df[cat] == 1, column_name] = ratios[cat][0]
            df.ix[df[cat] == 0, column_name] = -ratios[cat][1]
        else:
            df.ix[df[cat] == 1, column_name] = -ratios[cat][0]
            df.ix[df[cat] == 0, column_name] = ratios[cat][1]

  filters = ['certification','type']
  for col in df.columns:
      if col in filters:
          target = target_movie[col].iloc[0]
          df.ix[df[col] == target, 'adj_' + col] = 1
          df.ix[df[col] != target, 'adj_' + col] = 0

  path = os.path.join(os.getcwd(), "data", "{0}_output.csv".format(movie_id))
  df.to_csv(path)



# Calculate('tt2084970')
