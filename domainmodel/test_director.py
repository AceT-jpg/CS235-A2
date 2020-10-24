import pytest
from domainmodel.movie import Movie
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.review import Review

class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_eq(self):
        director1 = Director(None)
        director2 = Director("Michael Bay")
        director3 = Director("Taika Waititi")
        assert director2.__eq__(director3) == False
        assert director3.__eq__(director3) == True
        assert director1.__eq__(director3) == False

    def test_lt(self):
        director1 = Director("Cameron Diaz")
        director2 = Director("Angelina Jolie")
        director3 = Director("Brad Pitt")
        assert director2.__lt__(director1) == True
        assert director3.__lt__(director1) == True
        assert director2.__lt__(director3) == True
        assert director3.__lt__(director2) == False
        assert director2.__lt__(director1) == True

    def test_hash(self):
        director1 = Director(None)
        director2 = Director("Mic Bay")
        director3 = Director("Taika Waitiafti")
        assert director1.__hash__() == 0
        assert director2.__hash__() == 7
        assert director3.__hash__() == 15



