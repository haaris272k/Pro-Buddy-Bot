from bs4 import BeautifulSoup
from constants import *
from connectTodatabase import *
import json
import requests
import random
import time
import telebot


# creating an instance of the TeleBot class
bot = telebot.TeleBot(BOT_API_KEY)
# bot = telebot.TeleBot("") For when u'll create a new vbot

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
        + l4
        + "\n"
        + "\n"
        + l5
        + "\n"
        + "\n"
        + "Thank you 😇"
        + "\n"
        + "\n"
        + "Developed by @Haaris272k",
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

    ############## scraping the news data which will be send to the user ##############

    r = requests.get(TRENDING_NEWS_LINK)

    soup = BeautifulSoup(r.text, "html.parser")

    news = soup.find_all("h3", {"class": "trenz_news_head lh22 listing_story_title"})

    trending_news = []

    for i in news:

        trending_news.append(i.get_text())

    final_display = " "

    for j in trending_news[0:10]:

        final_display = final_display + "🗞" + " " + j + "\n" + "\n"

    ###################################################################################

    # sending the relevant data to the telegram user
    interactive_tn_response = random.choice(interactive_news_response)
    bot.send_message(message.chat.id, interactive_tn_response)
    time.sleep(0.5)
    bot.send_message(message.chat.id, final_display)


"""function to send weather update to the user"""


@bot.message_handler(commands=["wu"])
def weather_update(message):

    ############## getting the weather data which will be send to the user ##############

    r = requests.get(WEATHER_UPDATE_LINK, headers=HEADERS)

    soup = BeautifulSoup(r.text, "html.parser")

    temperature = soup.find(
        "span", {"class": "CurrentConditions--tempValue--3a50n"}
    ).get_text()

    weather = "The current temperature is" + " " + temperature + "C"

    ######################################################################################

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, weather)


"""function to send a random joke to the user"""


@bot.message_handler(commands=["fun"])
def joke(message):

    # sending interactive response to the telegram user
    bot.send_message(
        message.chat.id,
        random.choice(interactive_joke_response),
    )

    """
    fetching random joke from the database and sending it to the telegram user.
    Using 'random' function to get a random number to be used as an ID.
    The Joke corresponding to that particular ID will be fetched from the database 
    and sent to the telegram user. Same will be done for quote, fact and poem functions
    
    """

    """Remove the docstring of the below code if in case,
    the id doesn't exist in the database"""

    """
    try:
        id = random.randint(1, 1000)
        query = collection.find_one({"_id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["joke"])
    except:
        id = random.randint(1, 1000)
        query = collection.find_one({"_id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["joke"])
    
    """
    id = random.randint(1, 1000)
    query = collection.find_one({"_id": id})
    time.sleep(0.5)
    bot.send_message(message.chat.id, query["joke"])


"""function to send a random meme to the user"""


@bot.message_handler(commands=["meme"])
def meme(message):

    """Remove the docstring of the below code if in case,
    the id doesn't exist in the database"""

    """
    try:
        id = random.randint(1391, 1840)
        query = collection.find_one({"id": id})
        time.sleep(0.5)
        bot.send_photo(message.chat.id, query["meme"])
    except:
        id = random.randint(1391, 1840)
        query = collection.find_one({"id": id})
        time.sleep(0.5)
        bot.send_photo(message.chat.id, query["meme"])
    
    """
    id = random.randint(1391, 1840)
    query = collection.find_one({"id": id})
    time.sleep(0.5)
    bot.send_photo(message.chat.id, query["meme"])


"""function to send a random poem to the user"""


@bot.message_handler(commands=["lit"])
def poem(message):

    """Remove the docstring of the below code if in case,
    the id doesn't exist in the database"""

    """
    try:
        id = random.randint(1163, 1187)
        query = collection.find_one({"id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["poem"])
    except:
        id = random.randint(1163, 1187)
        query = collection.find_one({"id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["poem"])
    """
    id = random.randint(1163, 1187)
    query = collection.find_one({"_id": id})
    time.sleep(0.5)
    bot.send_message(message.chat.id, query["poem"])


"""function to send a random quote to the user"""


@bot.message_handler(commands=["quote"])
def quote(message):

    """Remove the docstring of the below code if in case,
    the id doesn't exist in the database"""

    """
    try:
        id = random.randint(1007, 1148)
        query = collection.find_one({"_id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["quote"])
    except:
        id = random.randint(1007, 1148)
        query = collection.find_one({"_id": id})
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["quote"])
    """
    id = random.randint(1007, 1148)
    query = collection.find_one({"_id": id})
    time.sleep(0.5)
    bot.send_message(message.chat.id, query["quote"])


# sending a random fact functionality
@bot.message_handler(commands=["fact"])
def fact(message):

    """Remove the docstring of the below code if in case,
    the id doesn't exist in the database"""

    """
    try:
        id = random.randint(1203, 1388)
        query = collection.find_one({"_id": id})
        bot.send_message(message.chat.id, "Here's a fact for you...")
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["fact"])
    except:
        id = random.randint(1203, 1388)
        query = collection.find_one({"_id": id})
        bot.send_message(message.chat.id, "Here's a fact for you...")
        time.sleep(0.5)
        bot.send_message(message.chat.id, query["fact"]) 
    """
    id = random.randint(1203, 1388)
    query = collection.find_one({"_id": id})
    bot.send_message(message.chat.id, interactive_fact_response)
    time.sleep(0.5)
    bot.send_message(message.chat.id, query["fact"])


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
        link = f"https://www.omdbapi.com/?t={movie_title}&apikey={MOVIESDB_API_KEY}"
        r = requests.get(link, headers=HEADERS)

        # parsing the data and converting it (from json data format) to a dictionary
        movie_data = json.loads(r.text)

        # accessing the required data
        movie_genre = movie_data["Genre"]
        movie_title = movie_data["Title"]
        movie_year = movie_data["Year"]
        movie_rating = movie_data["imdbRating"]
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

    ############## scraping the relevant data which will be send to the user ##############

    r = requests.get(WESTERN_SONGS_LINK, headers=HEADERS)

    soup = BeautifulSoup(r.text, "html.parser")

    extracting = soup.find(
        "div",
        {
            "class": "chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max"
        },
    ).find_all("h3", {"id": "title-of-a-story"})

    songs = []

    for song in extracting:

        songs.append(song.get_text().strip())

    list_songs = songs[2:12]

    top_10_western = " "

    for i in range(len(list_songs)):

        top_10_western = top_10_western + f"{i+1}" + " " + list_songs[i] + "\n" + "\n"

    #######################################################################################

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, "Here's the 10 western songs topping the chart 🎶")
    time.sleep(0.5)
    bot.send_message(message.chat.id, top_10_western)


"""function to display top 10 trending bollywood songs"""


@bot.message_handler(commands=["topb"])
def top_bollywood_songs(message):

    ############## scraping the relevant data which will be send to the user ##############

    r = requests.get(BOLLYWOOD_SONGS_LINK, headers=HEADERS)

    soup = BeautifulSoup(r.text, "html.parser")

    extracting = soup.find_all("a", {"class": "u-color-js-gray"})

    songs = []

    for song in extracting:

        songs.append(song.get_text().strip())

    list_songs = songs[0:10]

    top_10_bollywood = " "

    for i in range(len(list_songs)):

        top_10_bollywood = (
            top_10_bollywood + f"{i+1}" + " " + list_songs[i] + "\n" + "\n"
        )

    #######################################################################################

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
    bot.send_animation(message.chat.id, INVALID_INPUT_GIF, caption="Invalid command!")


bot.infinity_polling()
