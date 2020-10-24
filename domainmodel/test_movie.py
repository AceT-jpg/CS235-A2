import pytest
from domainmodel.movie import Movie
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.review import Review

class TestDirectorMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        print(movie)

        director = Director("Ron Clements")
        movie.director = director
        print(movie.director)
        movie.description = ""
        print(movie.description)


        actors = [Actor("Auli'i Cravalho"), Actor(1), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        print(movie.actors)

        genres = [Genre("Kids"), Genre("Horror"), Genre("Romance"), Genre(1)]
        for g in genres:
            movie.add_genre(g)
        print(movie.genres)

        movie.runtime_minutes = 104
        print("Movie runtime: {} minutes".format(movie.runtime_minutes))

        movie1 = Movie("Avengers", 2019)
        print(movie1)

        actors1 = "test"
        movie1.actors = actors1
        print(movie1.actors)

        director1 = Director("Stan Lee")
        movie1.director = director1
        movie.director = director1
        print(movie.director)
        print(movie1.director)

        print(movie == movie1)
        print(movie == movie)
        print(movie < movie1)

        movies = [movie, movie1]
        movies.sort()
        print(movies)


    def test_(self):
        movie1 = Movie("Moana", 2016)
        assert repr(movie1) == "<Movie Moana, 2016>"

    def test_eq(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Split", 2016)
        movie3 = Movie("Money", 2017)
        movie4 = Movie("Melon", 2016)
        assert movie1.__eq__(movie2) == False
        assert movie1.__eq__(movie3) == False
        assert movie1.__eq__(movie4) == True

    def test_lt(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Split", 2016)
        movie3 = Movie("Moana", 1999)
        assert movie1.__lt__(movie2) == True
        assert movie1.__lt__(movie3) == False

    def test_hash(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Moana" , None)
        assert movie1.__hash__() == 9
        assert movie2.__hash__() == 5
