# Creaţi o colecţie de date numită Filme în care vor exista documente cu următoarele informaţii:
# titlul filmului;
# genul filmului;
# anul lansării.
# Trebuie să prezentaţi inserarea documentelor în colecţie, precum şi citirea tuturor documentelor din colecţie.
import pymongo

class Movie():
    
    def __init__(self, title, genre, year) -> None:
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self):
        return f'{self.title} - {self.genre} - {self.year}'
    
    def __eq__(self, other):
        m1 = hash(self.title + self.genre + str(self.year))
        m2 = hash(other.title + other.genre + str(other.year))
        return m1 == m2
    


class MovieCollection():
    def __init__(self, database_name):
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn[database_name]
        self.collection = db.moviesCollection

    def insertMovie(self, *args):
        for movie in args:
            is_in_collection = False
            for m in self.collection.find():
                mv = Movie(m['title'], m['genre'], m['year'])
                if mv == movie:
                    is_in_collection = True

            if not is_in_collection:
                movie_details = {'title' : movie.title, 'genre' : movie.genre, 'year' : movie.year}
                self.collection.insert_one(movie_details)
            else:
                print('Movie already in the db...')

    
    def listAllMovies(self) -> str:
        for movie in self.collection.find():
            print(f"Title: {movie['title']} - Genre: {movie['genre']} - Year: {movie['year']} ")


if __name__ == '__main__':
    c = MovieCollection('Movies')
    
    m1 = Movie('Salutare de la mare', 'Comedy', 1995)
    m2 = Movie('Fight Club', 'Action', 2005)

    c.insertMovie(m1, m2)
    c.listAllMovies()

