from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from datafilereaders.login_data_csv_reader import LoginDataCSVReader
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.movie import Movie
from flask import Flask, redirect, url_for, render_template, request

loggedin = False

def login():
    app = Flask(__name__)
    movie_filename = 'datafiles/Data1000Movies.csv'
    login_filename = 'datafiles/LoginData.csv'
    login_file_reader = LoginDataCSVReader(login_filename)
    login_file_reader.read_csv_file()
    movie_file_reader = MovieFileCSVReader(movie_filename)
    movie_file_reader.read_csv_file()


    @app.route("/", methods=["POST", "GET"])
    def login_home():
        if request.method == "POST":
            if request.form.get("Login") == "do":
                username = request.form["user"]
                password = request.form["password"]
                for user in login_file_reader.dataset_of_users:
                    if user.user_name == username.lower():
                        if user.password == password:
                            return redirect(url_for("home", usr=username))
                return render_template("login_home.html")
            elif request.form.get("Register") == "do":
                username = request.form["user"]
                password = request.form["password"]
                if str(username) in login_file_reader.dataset_of_usernames:
                    return render_template("login_home.html", text="Error: User already exists in database!")
                else:
                    login_file_reader.add_user(username, password)
                    login_file_reader.read_csv_file()
                    return render_template("login_home.html", text="Register Successful!")
        else:
            return render_template("login_home.html")



    @app.route("/Home <usr>", methods=["POST", "GET"])
    def home(usr):
        if request.method == "POST":
            if request.form.get("Movie Name Search") == "do":
                movie_name = request.form["mv"]
                for movie in movie_file_reader.dataset_of_movies:
                    actors = []
                    genres = []
                    for actor in movie.actors:
                        actors.append(actor.actor_full_name)
                    for genre in movie.genres:
                        genres.append(genre.genre_name)
                    if movie.title() == movie_name:
                        return render_template("MovieSearch.html", name=movie_name + " Movie Information",
                                               director=movie.director.director_full_name, year=movie.year(),
                                               runtime=str(movie.runtime_minutes) + " minutes",
                                               genre=', '.join([str(x) for x in genres]),
                                               actors=', '.join([str(x) for x in actors]), desc=movie.description)
                return render_template("MovieSearch.html", name=movie_name + " movie was not found!", director="N/A",
                                       year="N/A", runtime="N/A", genre="N/A", actors="N/A", desc="N/A")
            elif request.form.get("Director Name Search") == "do1":
                director_name = request.form["mv"]
                for director in movie_file_reader.dataset_of_directors:
                    if director.director_full_name == director_name:
                        movies = []
                        for movie in movie_file_reader.dataset_of_movies:
                            if movie.director == director:
                                movies.append(movie.title())
                        return render_template("DirectorSearch.html", name=director.director_full_name+" Director Information", movies=', '.join([str(x) for x in movies]))
                return render_template("DirectorSearch.html", name=director_name+" director was not found!", movies="N/A")
            elif request.form.get("Actor Name Search") == "do2":
                actor_name = request.form["mv"]
                for actor in movie_file_reader.dataset_of_actors:
                    if actor.actor_full_name == actor_name:
                        movies = []
                        for movie in movie_file_reader.dataset_of_movies:
                            if actor in movie.actors:
                                movies.append(movie.title())
                        return render_template("ActorSearch.html", name=actor.actor_full_name+" Actor Information", movies=', '.join([str(x) for x in movies]))
                return render_template("ActorSearch.html", name=actor_name+" actor was not found!", movies="N/A")
            elif request.form.get("Genre Category Search") == "do3":
                genre_name = request.form["mv"]
                count = 0
                movies = []
                for genre in movie_file_reader.dataset_of_genres:
                    if genre.genre_name == genre_name:
                        for movie in movie_file_reader.dataset_of_movies:
                            if genre in movie.genres:
                                movies.append(movie.title())
                        return render_template("GenreSearch.html", name=genre_name + " Genre Information", movies=', '.join([str(x) for x in movies]), movies1=movies, int=count)
                    if request.form.get("next") == "do":
                        count += 5
                        return "Yes!"
                    elif request.form.get("prev") == "do":
                        count -= 5
                        return render_template("GenreSearch.html", name=genre_name + " Genre Information", movies=', '.join([str(x) for x in movies]), movies1=movies, int=count)
                return render_template("GenreSearch.html", name=genre_name+" genre was not found!", movies="N/A", movies1=movies, int=count)
        else:
            return render_template("Home.html", name=usr, movies=None, total=0, reviews=0)

    app.run(debug=True)



login()