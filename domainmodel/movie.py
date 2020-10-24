from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title, year):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if year == "" or type(year) is not int or year < 1900:
            self.__year = None
        else:
            self.__year = year
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0


    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if self.__title[0] == other.__title[0]:
            if self.__year == other.__year:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.__title == None:
            if other.__title == None:
                return False
        elif other.__title == None:
            return True
        elif self.__title == None:
            return False
        elif self.__title[0] == other.__title[0]:
            return self.__year < other.__year
        else:
            return self.__title[0] < other.__title[0]

    def __hash__(self):
        if self.__title == None:
            return 0
        elif self.__year == None:
            return hash(len(self.__title))
        else:
            return hash(len(self.__title)) + hash(len(str(self.__year)))

    def title(self):
        return self.__title

    def year(self):
        return self.__year

    def add_actor(self, a):
        if isinstance(a, Actor) == True:
            self.__actors.append(a)
        else:
            pass

    def remove_actor(self, a):
        if isinstance(a, Actor) == True:
            if a in self.__actors:
                self.__actors.remove(a)
        else:
            pass

    def add_genre(self, g):
        if isinstance(g, Genre) == True:
            self.__genres.append(g)
        else:
            pass

    def remove_genre(self, g):
        if isinstance(g, Genre) == True:
            if g in self.genres:
                self.__genres.remove(g)
        else:
            pass

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if isinstance(runtime_minutes, int) == True:
            if runtime_minutes > 0:
                self.__runtime_minutes = runtime_minutes
            else:
                raise ValueError("Runtime mintues MUST be positive")
        else:
            pass

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, a):
        if isinstance(a, list) == True:
            if a == []:
                self.__actors = None
            else:
                self.__actors = a
        else:
            self.__actors = None

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, d: Director):
        if isinstance(d, Director) == True:
            if self.__director is None:
                self.__director = d
            else:
                pass

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, g):
        if isinstance(g, list) == True:
            if g == []:
                self.__genres = None
            else:
                self.__genres = g
        else:
            self.__genres = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str) == True:
            if description == "":
                pass
            else:
                self.__description = description.strip()






