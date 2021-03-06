import media
import fresh_tomatoes

# toy story movie: title, storyline, poster image and trailer
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# emoji movie: title, storyline, poster image and trailer
emoji_movie = media.Movie("Emoji Movie",
                          "A story about emojis",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V",
                          "https://youtu.be/c_8cbx_jOmw")

# the godfather movie: title, storyline, poster image and trailer
the_godfather = media.Movie("The Godfather",
                            "A story of an Italian family up to no good",
                            "http://pannonia-entertainment.com/wp-content/uploads/2016/03/god_1.jpg",
                            "https://youtu.be/sY1S34973zA")

# lord of the rings movie: title, storyline, poster image and trailer
fellowship = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                         "A story about a fellowship of the ring",
                         "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=V75dMMIW2B4")

# set the movies which will be passed into the media file
movies = [toy_story, emoji_movie, the_godfather, fellowship]

# open the HTML file in a web browser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
