import pytest
from domainmodel.movie import Movie
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.review import Review

class TestDirectorMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(42)
        assert genre3.genre_name is None

    def test_eq(self):
        genre1 = Genre(None)
        genre2 = Genre("Romance")
        genre3 = Genre("Sci-Fi")
        assert genre2.__eq__(genre3) == False
        assert genre3.__eq__(genre3) == True
        assert genre1.__eq__(genre3) == False

    def test_lt(self):
        genre1 = Genre("Comedy")
        genre2 = Genre("Action")
        genre3 = Genre("Bollywood")
        assert genre2.__lt__(genre1) == True
        assert genre3.__lt__(genre1) == True
        assert genre2.__lt__(genre3) == True
        assert genre3.__lt__(genre2) == False
        assert genre2.__lt__(genre1) == True

    def test_hash(self):
        genre1 = Genre(None)
        genre2 = Genre("Action")
        genre3 = Genre("Romcom")
        assert genre1.__hash__() == 0
        assert genre2.__hash__() == 6
        assert genre3.__hash__() == 6

TestDirectorMethods()