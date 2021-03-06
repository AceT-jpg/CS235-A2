
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        if self.__director_full_name == None:
            if other.__director_full_name == None:
                return False
        if other.__director_full_name == None:
            return True
        if self.__director_full_name == None:
            return False
        else:
            return self.__director_full_name[0] < other.__director_full_name[0]

    def __hash__(self):
        if self.__director_full_name == None:
            return 0
        else:
            return hash(len(self.__director_full_name))

