# Creaţi o colecţie de date numită Filme în care vor exista documente cu următoarele informaţii:
# titlul filmului;
# genul filmului;
# anul lansării.
# Trebuie să prezentaţi inserarea documentelor în colecţie, precum şi citirea tuturor documentelor din colecţie.


import pymongo
import datetime
from menu import Menu

def db_collection(database_name):
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn[database_name]
    return db.moviesCollection

def insertMovie(collection, new_movie):
    is_not_ok = False
    for m in collection.find():
        if m['title'] == new_movie['title']:
            is_not_ok = True
            print('Movie already in the db...')
        if not new_movie['year'] in range(1940, datetime.datetime.now().year):
            is_not_ok = True
            print(f"Incorrect year for the movie {new_movie['title']}...")
    if not is_not_ok:
        collection.insert_one(new_movie)

def get_new_movie():
    title = input('Input title: ')
    genre = input('Input genre: ')
    year = int(input('Input year: '))
    movie = {'title':title, 'genre':[genre, ], 'year':year}
    return movie

def add_genre(collection, title, new_genre):
    is_not_ok = False
    for m in collection.find():
        if m['title'] == title and new_genre in m['genre']:
            is_not_ok = True
            print('Genre already assigned to this movie...')
    if not is_not_ok:
        collection.update_one({'title':title}, {'$push': {'genre': new_genre}})
        print(f'{new_genre} genre added to movie {title}...')

def listAllMovies(collection):
    for movie in collection.find():
        print(f"Title: {movie['title']} - Genre: {movie['genre']} - Year: {movie['year']} ")

def main():
    collection = db_collection('Movies')
    menu = Menu()
    while True:
        menu.show()
        option = menu.get_option
        if option == '1':
            listAllMovies(collection)
        elif option == '2':
            insertMovie(collection, get_new_movie())
        elif option =='3':
            movie_title = input('For witch movie you want to add new genre? ')
            new_genre = input('Input new genre: ')
            add_genre(collection, movie_title, new_genre)
        input('Press ENTER to continue...')

if __name__ == '__main__':
    main()