from fcc_book_recommendation_knn import get_recommends
'''
def test_book_recommendation():
  test_pass = True
  book_title = input("Enter the title of a book: ")
  recommends = get_recommends(book_title)
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2): 
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    else:
        print(recommends[1][i][0])
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
    else:
        recommends[1][i][1]
    
  if test_pass:
    print("You passed the challenge!")
  else:
    print("You haven't passed yet. Keep trying!")
'''
def test_book_recommendation():
  book_title = input("Enter the title of a book: ")
  recommends = get_recommends(book_title)  
  print(recommends[1])    
  
if __name__ == "__main__":
   test_book_recommendation()