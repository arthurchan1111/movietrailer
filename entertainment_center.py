import media
import fresh_tomatoes


your_name = media.Movie("Your Name", "A Story of a Boy and Girl Switching Bodies",
                        "https://myanimelist.cdn-dena.com/images/anime/9/77484l.jpg",
                        "https://youtu.be/hRfHcp2GjVI")

walle = media.Movie("WALL-E", "A Sentient Robot's Adventures",
                    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")

up = media.Movie("UP", "An Old Man's Adventure",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

spirited_away = media.Movie("Spirited Away", "A Girl's Adventure in a Magical Land",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NTM1NTg1Ml5BMl5BanBnXkFtZTgwOTgzMTMyMDE@._V1_UY268_CR6,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

graveoftheFireFlies = media.Movie("Grave of the Fireflies",
                                  "A Young Boy and His Sister's struggle during the aftermath of World War 2",
                                  "http://static.rogerebert.com/uploads/movie/movie_poster/grave-of-the-fireflies-1988/large_bwVhmPpydv8P7mWfrmL3XVw0MV5.jpg", "https://www.youtube.com/watch?v=4vPeTSRd580")

gardenofwords = media.Movie("The Garden of Words", "A 15 Year Old Boy's unlikely friendship with a young women",
                            "https://upload.wikimedia.org/wikipedia/en/c/c3/Garden_of_Words_poster.png", "https://www.youtube.com/watch?v=udDIkl6z8X0")

movielist = [your_name, walle, up, spirited_away,
             graveoftheFireFlies, gardenofwords]

fresh_tomatoes.open_movies_page(movielist)
