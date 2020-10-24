from datafilereaders.login_data_csv_reader import LoginDataCSVReader

class TestLoginDataCSVReader:
    def test(self):
        filename = 'datafiles/LoginData.csv'
        login_data_reader = LoginDataCSVReader(filename)
        login_data_reader.read_csv_file()

        print(f'number of unique users: {len(login_data_reader.dataset_of_users)}')

    def test_2(self):
        filename = 'datafiles/LoginData.csv'
        login_data_reader = LoginDataCSVReader(filename)
        login_data_reader.read_csv_file()

        all_users_sorted = sorted(login_data_reader.dataset_of_usernames)
        print(all_users_sorted)
        print(f'first 3 unique directors of sorted dataset: {all_users_sorted[0:3]}')