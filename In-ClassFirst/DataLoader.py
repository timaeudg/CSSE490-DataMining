__author__ = 'timaeudg'

import pandas as pd

user_columns = ['id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=user_columns)

ratings_columns = ['id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=ratings_columns)

movie_columns = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=movie_columns)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')

number_of_ratings = data.groupby('title').size()
widely_viewed = number_of_ratings.index[number_of_ratings >= 250]
mean_ratings_filtered = mean_ratings.ix[widely_viewed]

top_female_ratings = mean_ratings_filtered.sort_index(by="F", ascending=False)

mean_ratings_filtered['diff'] = mean_ratings_filtered['M'] - mean_ratings_filtered['F']

biggest_difference = mean_ratings_filtered.sort_index(by="diff", ascending=True)

display_table = biggest_difference
print(display_table.head())