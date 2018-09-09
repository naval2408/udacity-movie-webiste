"""The script will create movie objects and open a webpage displaying them in a Grid"""
import fresh_tomatoes
import media

def main():
    """Create movie objects of different movies"""
    stree = media.Movie("Stree",
                          "A town is held in the grip of terror by tales of a mysterious woman.",
                          "https://res.cloudinary.com/firstpost/image/upload/q_auto,f_auto,fl_lossy/nw18-firstpost/2018/07/stree-int.jpg",
                          "https://www.youtube.com/watch?v=gzeaGcLLl_A")

    gold = media.Movie("Gold",
                          "After gaining independence, India wins its first Olympic gold medal in 1948.",
                          "https://images.assettype.com/thequint%2F2018-06%2F4e70ccdc-3886-4d57-80a8-90303417e05c%2Fgold_poster.jpg?q=35&auto=format%2Ccompress&w=1200",
                          "https://www.youtube.com/watch?v=Pcv0aoOlsLM")

    sui_dhaga = media.Movie("Sui Dhaga",
                           "An unemployed small-town man starts his own garment business.",
                           "https://i0.wp.com/indreport.com/wp-content/uploads/2018/08/Sui-dhaga-Trailer.png",
                           "https://www.youtube.com/watch?v=VUe3p23AJMo")

    blackmail = media.Movie("Blackmail",
                         "When Dev discovers his wife has been cheating on him, he decides to blackmail her.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/3/33/Blackmail_%282018_film%29.jpg/220px-Blackmail_%282018_film%29.jpg",
                         "https://www.youtube.com/watch?v=aPpLOfK_Z3A")

    mulk = media.Movie("Mulk",
                           "The struggles of a Muslim family after a member takes to terrorism.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Mulk_-_2018_Movie_Poster.jpg/220px-Mulk_-_2018_Movie_Poster.jpg",
                           "https://www.youtube.com/watch?v=tZnpy_D4m_Y")

    newton = media.Movie("Newton",
                          "A government clerk tries to run a free and fair election in a conflict area",
                          "https://upload.wikimedia.org/wikipedia/en/6/68/Newton_%28film%29.png",
                          "https://www.youtube.com/watch?v=yU6zMPFd4UU")

    movies = [stree, gold, sui_dhaga, blackmail, mulk, newton]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
