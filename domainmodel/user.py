from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, user_name, password):
        if isinstance(user_name, str):
            self.__user_name = user_name.strip().lower()
        else:
            user_name = None
        if isinstance(password, str):
            self.__password = password
        else:
            passwod = None
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name, str):
            self.__user_name = user_name.strip().lower()
        else:
            pass

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if isinstance(password, str):
            self.__password = password
        else:
            pass

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if isinstance(watched_movies, list):
            self.__watched_movies = watched_movies
        else:
            pass

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        if isinstance(reviews, list):
            self.__reviews = reviews
        else:
            pass

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes):
        if isinstance(time_spent_watching_movies_minutes, int):
            if time_spent_watching_movies_minutes > 0:
                self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes
            else:
                pass
        else:
            pass

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(len(self.__user_name))

    def watch_movie(self, movie):
        if isinstance(movie, Movie):
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
        else:
            pass

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)