# Dictionary mapping participants' names to their favourite movies
favourite_movies = {
    "Presenter": "Inception"
}


def display_favourite_movies():
    """
    Function to print each participant's favourite movie.
    """
    for name, movie in favourite_movies.items():
        print(f"{name}'s favourite movie: {movie}")


if __name__ == "__main__":
    display_favourite_movies()
