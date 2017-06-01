import media
import fresh_tomatoes

# calling the constructor media.Movie() to instantiate movie objects
avatar = media.Movie(
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "Avatar",
    "http://www.impawards.com/2009/posters/avatar.jpg"
)

blue_streak = media.Movie(
    "https://www.youtube.com/watch?v=kj5NHXDvKKM",
    "Bue Streak",
    "http://www.impawards.com/1999/posters/blue_streak.jpg"
    )

taxi = media.Movie(
    "https://www.youtube.com/watch?v=BBnlCXi2WWA",
    "Taxi",
    "http://img.moviepostershop.com/taxi-movie-poster-1998-1020475613.jpg"
    )

forrest_gump = media.Movie(
    "https://www.youtube.com/watch?v=YNh9Es8Ut6U",
    "Forrest Gump",
    "http://2.bp.blogspot.com/-u3wdo9w_k40/Us2Z7bdGKPI/AAAAAAAAPw8/M-Nktd8nMUI/s1600/forrest-gump-movie-poster-1994-1020190695.jpg"  # NOQA
    )

big_fish = media.Movie(
    "https://www.youtube.com/watch?v=dF-Iy7vIOJA",
    "Big Fish",
    "https://upload.wikimedia.org/wikipedia/zh/6/68/Big_Fish_movie.jpg"
    )

the_galaxy = media.Movie(
    "https://www.youtube.com/watch?v=d96cjJhvlMA",
    "Guardians of the Galaxy",
    "http://nerdsontherocks.com/wp-content/uploads/2015/02/Guardians-of-the-Galaxy.jpg"  # NOQA
    )

# Store all those movie instance in a list data structure
movies = [avatar, blue_streak, taxi, forrest_gump, big_fish, the_galaxy]

# Input the movies list to open_movies_page() function to build the HTML file
fresh_tomatoes.open_movies_page(movies)
