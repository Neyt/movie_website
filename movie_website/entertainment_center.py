# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

Jiro = media.Movie("Jiro Dreams of Sushi", "http://ecx.images-amazon.com/images/I/810Fw8dOh4L._SL1500_.jpg", "https://www.youtube.com/watch?v=I1UDS2kgqY8")
print (Jiro.trailer_youtube_url)
TED_Talks = media.Movie("TED Talks: Life Hacks", "http://bingeout.com/wp-content/uploads/2015/06/FluidStance_Ted-Talks-689x400.png", "https://youtu.be/bhPfzTvqFTU")
print (TED_Talks.trailer_youtube_url)
Joan_Rivers = media.Movie("Joan Rivers: A Piece of Work", "http://www.chicagonow.com/blogs/life-and-times-of-a-young-republican/jriverspieceofworkposter.jpg", "https://youtu.be/2fnojZw54ls")
print (Joan_Rivers.trailer_youtube_url)
Enron = media.Movie("Enron: The Smartest Guys in the Room", "http://ecx.images-amazon.com/images/I/51G61Y9SGAL.jpg", "https://youtu.be/-w6duQhWuVk")
print (Enron.trailer_youtube_url)
American_Experience = media.Movie("American Experience: Henry Ford", "http://old.seattletimes.com/ABPub/2013/01/28/2020232995.jpg", "https://youtu.be/smyMT2pnLbQ")
print (American_Experience.trailer_youtube_url)
movies = [Jiro, TED_Talks, Joan_Rivers, Enron, American_Experience]
fresh_tomatoes.open_movies_page(movies)
