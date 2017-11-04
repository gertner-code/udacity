from media import Movie
import webbrowser
import fresh_tomatoes


# calls to Movie initializing each instance with the correct data
ghost_in_the_shell = Movie(
    "Ghost in the Shell",
    "A cyborg policewoman and her partner hunt a mysterious and powerful "
    "hacker called the Puppet Master.",
    "https://images.fandango.com/ImageRenderer/300/0/redesign/static/img/default_poster.png/0/images/masterrepository/Fandango/728/gits-400x600.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SvBVDibOrgs&feature=youtu.be&t=8s"
    )

shawshank = Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and "
    "eventual redemption through acts of common decency.",
    "https://images-na.ssl-images-amazon.com/images/I/51SPVi-1rXL._SY450_.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco"
    )

dark_knight = Movie(
    "The Dark Knight",
    "When the menace known as the Joker emerges from his mysterious past, he "
    "wreaks havoc and chaos on the people of Gotham, the Dark Knight must "
    "accept one of the greatest psychological and physical tests of his "
    "ability to fight injustice.",
    "https://images-na.ssl-images-amazon.com/images/I/81AJdOIEIhL._SY550_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q"  # NOQA
    )

spirited_away = Movie(
    "Spirited Away",
    "During her family's move to the suburbs, a sullen 10-year-old girl "
    "wanders into a world ruled by gods, witches, and spirits, and where "
    "humans are changed into beasts.",

    "http://www.impawards.com/2002/posters/spirited_away.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ByXuk9QqQkk"  # NOQA
    )

fifth_element = Movie(
    "The Fifth Element",
    "In the colorful future, a cab driver unwittingly becomes the central "
    "figure in the search for a legendary cosmic weapon to keep Evil and Mr. "
    "Zorg at bay.",
    "https://2.bp.blogspot.com/-6P-3QgANlFY/UClxCfmUWPI/AAAAAAAALbY/PIX-FP7ujaM/s1600/The+Fifth+Element+%281997%29+4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=fQ9RqgcR24g"
    )

the_last_crusade = Movie(
    "Indiana Jones and the Last Crusade",
    "When Dr. Henry Jones, Sr. suddenly goes missing while pursuing the Holy "
    "Grail, eminent archaeologist Dr. Henry 'Indiana' Jones, Jr. must follow "
    "in his father's footsteps to stop the Nazis from getting their hands on "
    "the Holy Grail first.",
    "https://images-na.ssl-images-amazon.com/images/I/511AHRR6yKL._SY450_.jpg",
    "https://www.youtube.com/watch?v=a6JB2suJYHM"
    )

# list of all instances of Movie
movies = [
    ghost_in_the_shell, shawshank, dark_knight,
    spirited_away, fifth_element, the_last_crusade
    ]
# creates webpage using the above list
fresh_tomatoes.open_movies_page(movies)
