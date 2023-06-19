# import libraries (you may add additional imports but you may not have to)
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# get data files
#wget 'https://cdn.freecodecamp.org/project-data/books/book-crossings.zip'

#unzip 'book-crossings.zip'

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'
# import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})
# Remove users with < 200 ratings and books with < 100 ratings
df_ratings["rating"].fillna(0,inplace=True)

user_counts = df_ratings.groupby('user')["rating"].count()
book_counts =  df_ratings.groupby('isbn')["rating"].count()

fil_user_counts = user_counts[user_counts >= 200].index
df_user_counts = pd.DataFrame(fil_user_counts)

df_ratings = df_ratings.merge(df_user_counts, on="user")

fil_book_counts = book_counts[(book_counts >= 100)].index
df_book_counts = pd.DataFrame(fil_book_counts)

df_ratings = df_ratings.merge(df_book_counts, on="isbn")
df_ratings = df_ratings.merge(df_books, on="isbn")
df_ratings = df_ratings.drop_duplicates(['user', 'title'],keep="first")
piv = df_ratings.pivot(index='title', columns='user', values='rating')
piv = piv.fillna(0)
csr_mat = csr_matrix(piv)
# KNN Model Fitting
knn_model = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors=6)
nn = knn_model.fit(csr_mat)
#book_title = "Where the Heart Is (Oprah's Book Club (Paperback))"
book_title = "The Queen of the Damned (Vampire Chronicles (Paperback))"
# function to return recommended books - this will be tested
def get_recommends(book = ""):
  arr = np.array(piv.loc[book,:])
  distances, indices = nn.kneighbors(arr.reshape(1,-1), n_neighbors = 6)
  # Array format:
  #[book,[[book4,dist4],[book3,dist3],[book2,dist2],[book1,dist1]]
  
  return [book, [[piv.index.values[indices], distances] for indices, distances in zip(reversed(indices[0][1:6]), reversed(distances[0][1:6]))]]
books = get_recommends(book_title)

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2): 
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge!")
  else:
    print("You haven't passed yet. Keep trying!")
