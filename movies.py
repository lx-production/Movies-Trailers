import best_tomatoes  # Main code, contains functions to generate HTML file
import media  # Contains the Movie class

logan = media.Movie(
    "Logan",
    "The Wolverine meets a young mutant girl who is very much like him.",
    "http://www.beliefnet.com/columnists/moviemom/files/2017/03/logan.jpg",
    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

jungle_book = media.Movie(
    "The Jungle Book",
    "A story about a boy who grew up in the jungle",
    "http://i.imgur.com/jPnTp8b.jpg",
    "https://www.youtube.com/watch?v=5mkm22yO-bs")

the_great_wall = media.Movie(
    "The Great Wall",
    "Two foreigners found themselves stuck in a mystical war.",
    "https://assets.voxcinemas.com/posters/P_HO00004241.jpg",
    "https://www.youtube.com/watch?v=avF6GHyyk5c")

finding_dory = media.Movie(
    "Finding Dory",
    "Dory goes on a journey looking for her lost parents.",
    "http://i.imgur.com/85lqxTh.jpg",
    "https://www.youtube.com/watch?v=UXpe8-zCwhI")

scarface = media.Movie(
    "Scarface",
    "An immigrant Cuban man on his way to become"
    "the most powerful drug lord in the US.",
    "http://i.imgur.com/dfEq5dl.jpg",
    "https://www.youtube.com/watch?v=7pQQHnqBa2E")

casino_royal = media.Movie(
    "Casino Royal",
    "James Bond on another mission.",
    "http://www.gstatic.com/tv/thumb/movieposters/159167/p159167_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=fl5WHj0bZ2Q")


movies = [logan, jungle_book, the_great_wall,
          finding_dory, scarface, casino_royal]

# Run project
best_tomatoes.open_movies_page(movies)
