from constants import *
from database_handlers import *
from data_scraper import *
import json
import schedule
import time
import telebot


# creating an instance of the TeleBot class
bot = telebot.TeleBot(BOT_API_KEY)

# connecting to the database from DatabaseHandler class
dbhandler.connect_database(MONGODB_ATLAS_UNAME, MONGODB_ATLAS_PW)

"""function to welcome the user"""


@bot.message_handler(commands=["start"])
def hello(message):

    # welcoming the user
    bot.send_message(
        message.chat.id,
        l1
        + "\n"
        + "\n"
        + l2
        + "\n"
        + "\n"
        + l3
        + "\n"
        + "\n"
        + "Thank you 😇"
        + "\n"
        + "\n"
        + "Developed by @Haaris272k",
    )

    time.sleep(3)
    username = message.from_user.username
    bot.send_message(
        message.chat.id,
        f"Hey @{username}!, Do you want to get automated news updates?. Select /yes or /no",
    )


"""function to send automated news updates"""


@bot.message_handler(commands=["yes"])
def automated_trending_news(message):

    bot.send_message(
        message.chat.id, "Ok, You will be recieving automated news updates from now on!"
    )

    """send news updates to the user (similar to  as what /nu command does)"""

    def get_trending_news():

        # using get_news() method from scraper class to get the news
        news = data.get_news(TRENDING_NEWS_LINK)

        # sending the news to the user
        bot.send_message(message.chat.id, news)

    # scheduling the function to run every n minutes
    schedule.every(18000).seconds.do(get_trending_news)
    while True:
        schedule.run_pending()
        time.sleep(1)


@bot.message_handler(commands=["no"])
def no(message):

    # sending a message to the user
    bot.send_message(
        message.chat.id,
        "You can use /nu command manually to get news updates whenever you want.",
    )


"""function to list the available commands"""


@bot.message_handler(commands=["list"])
def list(message):

    # list of all the available commands
    comms = (
        "List of available commands:"
        + "\n"
        + "\n"
        + "/hi - to greet the bot."
        + "\n"
        + "\n"
        + "/nu - to view trending news of the day."
        + "\n"
        + "\n"
        + "/wu - to view the live weather update."
        + "\n"
        + "\n"
        + "/fun - to get something funny (humorous)."
        + "\n"
        + "\n"
        + "/meme - to get a random meme."
        + "\n"
        + "\n"
        + "/lit - to get a random writing/literary work/poem."
        + "\n"
        + "\n"
        + "/quote - to get a random quote."
        + "\n"
        + "\n"
        + "/fact - to get a random fact."
        + "\n"
        + "\n"
        + "/topw - top 10 trending western songs of the week."
        + "\n"
        + "\n"
        + "/topb -  top 10 trending bollywood songs of the week."
        + "\n"
        + "\n"
        + "/movie or /md - to get the details of any movie."
    )

    # sending the list of commands to the telegram user
    bot.send_message(message.chat.id, comms)


"""function to greet the user"""


@bot.message_handler(commands=["hello", "hi", "hey"])
def hello(message):

    # greeting the user
    username = str(message.chat.first_name)
    greet = random.choice(interactive_greet_response)
    bot.send_message(message.chat.id, f"Hey {username}, {greet}")


"""function to send news to the user"""


@bot.message_handler(commands=["nu"])
def trending_news(message):

    # using get_news() method from Data_Scraper class to get the news
    trending_news = data.get_news(TRENDING_NEWS_LINK)

    # sending the relevant data to the telegram user
    interactive_tn_response = random.choice(interactive_news_response)
    bot.send_message(message.chat.id, interactive_tn_response)
    time.sleep(0.5)
    bot.send_message(message.chat.id, trending_news)


"""function to send weather update to the user"""


@bot.message_handler(commands=["wu"])
def weather_update(message):

    # using get_weather_update() method from Data_Scraper class to get the weather update
    weather_update = data.get_weather_update(WEATHER_UPDATE_LINK)

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, weather_update)


"""function to send a random joke to the user"""


@bot.message_handler(commands=["fun"])
def joke(message):

    # sending interactive response to the telegram user
    bot.send_message(
        message.chat.id,
        random.choice(interactive_joke_response),
    )

    tagtype = "joke"

    """
    using lookup method of dbhandler class 
    to get a random joke from the database. 
    This lookup algorithm will be used in fetching other 
    data (meme, poem, quote, fact) as well.
    
    """
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


"""function to send a random meme to the user"""


@bot.message_handler(commands=["meme"])
def meme(message):

    tagtype = "meme"
    result = dbhandler.lookup(tagtype)
    bot.send_photo(message.chat.id, result)


"""function to send a random poem to the user"""


@bot.message_handler(commands=["lit"])
def poem(message):

    tagtype = "poem"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


"""function to send a random quote to the user"""


@bot.message_handler(commands=["quote"])
def quote(message):

    tagtype = "quote"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


"""function to send a random fact to the user"""


@bot.message_handler(commands=["fact"])
def fact(message):

    tagtype = "fact"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


"""function(s) to provide with the movie details"""


@bot.message_handler(commands=["Md", "md", "movie", "Movie"])
def ask_movie_name(message):

    # asking the user to enter the movie name
    display_message = "What movie do you want to know about?"
    bot.reply_to(message, display_message)
    bot.register_next_step_handler(message, get_movie_name)


def get_movie_name(message):

    # getting the movie name from the user
    movie_title = message.text

    try:
        # fetching the movie details from the API
        link = (
            f"https://www.omdbhandlerapi.com/?t={movie_title}&apikey={MOVIESDB_API_KEY}"
        )
        r = requests.get(link, headers=HEADERS)

        # parsing the data and converting it (from json data format) to a dictionary
        movie_data = json.loads(r.text)

        # accessing the required data
        movie_genre = movie_data["Genre"]
        movie_title = movie_data["Title"]
        movie_year = movie_data["Year"]
        movie_rating = movie_data["imdbhandlerRating"]
        movie_runtime = movie_data["Runtime"]
        movie_director = movie_data["Director"]
        movie_actors = movie_data["Actors"]
        movie_plot = movie_data["Plot"]
        movie_awards = movie_data["Awards"]

        # storing the movie details
        final_data = (
            f"Title: {movie_title} \n"
            f" \n"
            f"Genre: {movie_genre} \n"
            f" \n"
            f"Year: {movie_year} \n"
            f" \n"
            f"Rating: {movie_rating} \n"
            f" \n"
            f"Runtime: {movie_runtime} \n"
            f" \n"
            f"Director: {movie_director} \n"
            f" \n"
            f"Actors: {movie_actors} \n"
            f" \n"
            f"Plot: {movie_plot} \n"
            f" \n"
            f"Awards: {movie_awards} \n"
        )

        # sending the relevant data to the telegram user
        bot.send_message(message.chat.id, final_data)

    except:
        bot.send_message(message.chat.id, "Invalid movie name! ")


"""function to display top 10 trending western songs"""


@bot.message_handler(commands=["topw"])
def top_western_songs(message):

    # using get_trending_western_songs() method from Data_Scraper class to get the top 10 trending western songs
    top_10_western = data.get_trending_western_songs(WESTERN_SONGS_LINK)

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, "Here's the 10 western songs topping the chart 🎶")
    time.sleep(0.5)
    bot.send_message(message.chat.id, top_10_western)


"""function to display top 10 trending bollywood songs"""


@bot.message_handler(commands=["topb"])
def top_bollywood_songs(message):

    # using get_trending_bollywood_songs() method from Data_Scraper class to get the top 10 trending bollywood songs
    top_10_bollywood = data.get_trending_bollywood_songs(BOLLYWOOD_SONGS_LINK)

    # sending the relevant data to the telegram user
    bot.send_message(
        message.chat.id,
        "Let's see what's making buzz in the indian musical industry these days 😜",
    )
    time.sleep(2)
    bot.send_message(message.chat.id, top_10_bollywood)


"""function to display invalid command message"""


@bot.message_handler(func=lambda m: True)
def invalid_input(message):

    # sending 'invalid input!' message to the user along with the gif
    bot.send_animation(
        message.chat.id, INVALID_INPUT_GIF, caption="Unrecognizable command!"
    )


bot.infinity_polling()
