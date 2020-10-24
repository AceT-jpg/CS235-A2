from datetime import datetime
from domainmodel.movie import Movie

class Review:
    def __init__(self, movie, review_text, rating):
        if isinstance(movie, Movie) == True:
            self.__movie = movie
        else:
            self.__movie = None
        if isinstance(review_text, str) == True:
            self.__review_text = review_text
        else:
            self.__review_text = None
        if rating > 0 and rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    def __repr__(self):
        return f"<{self.__review_text}>"

    def __eq__(self, other):
        if self.__movie == other.__movie:
            if self.__rating == other.__rating:
                if self.__review_text == other.__review_text:
                    if self.__timestamp == other.__timestamp:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self.__movie = movie
        else:
            pass

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text):
        if isinstance(review_text, str):
            self.__review_text = review_text
        else:
            pass

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int):
            if rating > 0 and rating <= 10:
                self.__rating = rating
            else:
                pass
        else:
            pass

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if isinstance(timestamp, datetime):
            self.__timestamp = timestamp
        else:
            pass






