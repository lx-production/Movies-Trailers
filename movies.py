import best_tomatoes
import media

logan = media.Movie("Logan",
                        "The Wolferin meets a young mutant girl who is very much like him.",
                        "http://www.beliefnet.com/columnists/moviemom/files/2017/03/logan.jpg",
                        "https://www.youtube.com/watch?v=RH3OxVFvTeg")

jungle_book = media.Movie("The Jungle Book",
                     "A story about a boy who grew up in the jungle",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh",
                     "https://www.youtube.com/watch?v=5mkm22yO-bs")

the_great_wall = media.Movie("The Great Wall",
                             "Two foreigners found them self stuck in a mystical war at the Great Wall of China",
                             "https://assets.voxcinemas.com/posters/P_HO00004241.jpg",
                             "https://www.youtube.com/watch?v=avF6GHyyk5c")

finding_dory = media.Movie("Finding Dory",
                           "Dory goes on a journey looking for her lost parents with the help of Nemo and his dad.",
                           "http://vignette4.wikia.nocookie.net/pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg",
                           "https://www.youtube.com/watch?v=UXpe8-zCwhI")

scarface = media.Movie("Scarface",
                       "The road to power of a Cuban man",
                       "http://static.tvgcdn.net/rovi/showcards/movie/116910/thumbs/16956231_1300x1733.jpg",
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

casino_royal = media.Movie("Casino Royal",
                           "James Bond on another mission",
                           "http://www.gstatic.com/tv/thumb/movieposters/159167/p159167_p_v8_aa.jpg",
                           "https://www.youtube.com/watch?v=fl5WHj0bZ2Q")

movies = [logan, jungle_book, the_great_wall, finding_dory, scarface, casino_royal]

best_tomatoes.open_movies_page(movies)  #Run project

