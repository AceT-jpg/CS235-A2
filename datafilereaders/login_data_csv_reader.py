import csv
from domainmodel.user import User
from domainmodel.review import Review

class LoginDataCSVReader:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_users = set()
        self.__dataset_of_usernames = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            login_data_reader = csv.DictReader(csvfile)

            for row in login_data_reader:
                user = User(row['User'], row['Pass'])
                self.__dataset_of_users.add(user)
                self.dataset_of_usernames.append(row['User'])

    @property
    def dataset_of_users(self) -> list:
        return self.__dataset_of_users

    @property
    def dataset_of_usernames(self) -> list:
        return self.__dataset_of_usernames

    def add_user(self, usr, pwd):
        with open(self.__file_name, 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([usr, pwd])