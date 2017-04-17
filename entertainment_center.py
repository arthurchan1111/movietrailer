import media
import fresh_tomatoes

# Instantiate 6 instances of the Movie class in media file and added specific attributes for each movie

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
                            "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

graveoftheFireFlies = media.Movie("Grave of the Fireflies",
                                  "A Young Boy and His Sister's struggle during the aftermath of World War 2",
                                  "https://upload.wikimedia.org/wikipedia/en/a/a5/Grave_of_the_Fireflies_Japanese_poster.jpg", 
                                  "https://www.youtube.com/watch?v=4vPeTSRd580")

gardenofwords = media.Movie("The Garden of Words",
                            "A 15 Year Old Boy's unlikely friendship with a young women",
                            "https://upload.wikimedia.org/wikipedia/en/c/c3/Garden_of_Words_poster.png",
                            "https://www.youtube.com/watch?v=udDIkl6z8X0")

# Put all the movies into a list

movielist = [your_name, walle, up, spirited_away,
             graveoftheFireFlies, gardenofwords]

# Opens web page from fresh_tomatoes.py

fresh_tomatoes.open_movies_page(movielist)
