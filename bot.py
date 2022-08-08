from bs4 import BeautifulSoup
from data import *
import json
import requests
import random
import time
import telebot

# creating an instance of the TeleBot class
bot = telebot.TeleBot("")
# bot = telebot.TeleBot("") For when u'll create a new vbot

# welcome function
@bot.message_handler(commands=["start"])
def hello(message):

    # welcoming the user
    l1 = "Hello, My name is Harry. My official name is 'ProBuddyBot'."
    l2 = "I'm a telegram bot that can be your best Buddy in need."
    l3 = "I can provide you with necessary updates and do a lot more stuff."
    l4 = "Feel free to add me to your telegram groups and let others know about me"
    l5 = "Type '/list' to see all the available commands"
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


# list the available commands function
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
        + "/cu - to view the live cricket score."
        + "\n"
        + "\n"
        + "/joke - to get a random joke."
        + "\n"
        + "\n"
        + "/meme - to get a random meme."
        + "\n"
        + "\n"
        + "/poem - to get a random poem."
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


# greeting function
@bot.message_handler(commands=["hello", "hi", "hey"])
def hello(message):

    # greeting the user
    username = str(message.chat.first_name)
    greet = random.choice(interactive_greet_response)
    bot.send_message(message.chat.id, f"Hey {username}, {greet}")


# send trending news function
@bot.message_handler(commands=["nu"])
def trending_news(message):

    ############## getting the relevant data which is to be send by the bot ##############

    r = requests.get(trending_news_link)
    soup = BeautifulSoup(r.text, "html.parser")
    news = soup.find_all("h3", {"class": "trenz_news_head lh22 listing_story_title"})
    trending_news = []
    for i in news:
        trending_news.append(i.get_text())
    final_display = " "
    for j in trending_news[0:5]:
        final_display = final_display + "*" + " " + j + "\n" + "\n"

    ######################################################################################

    # sending the relevant data to the telegram user
    interactive_tn_response = random.choice(interactive_news_response)
    bot.send_message(message.chat.id, interactive_tn_response)
    time.sleep(0.5)
    bot.send_message(message.chat.id, final_display)


# send weather update function
@bot.message_handler(commands=["wu"])
def weather_update(message):

    ############## getting the relevant data which is to be send by the bot ##############

    r = requests.get(weather_update_link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    temperature = soup.find(
        "span", {"class": "CurrentConditions--tempValue--3a50n"}
    ).get_text()

    weather = "The current temperature is" + " " + temperature + "C"

    ######################################################################################

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, weather)


# send cricket update function
@bot.message_handler(commands=["cu"])
def cricket_update(message):

    ############## getting the relevant data which is to be send by the bot ##############

    try:
        r = requests.get(cricket_update_link)
        soup = BeautifulSoup(r.text, "html.parser")
        team_1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
        team_2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
        t1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
        t2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
        if t2_score == "" or t2_score[0] == " ":
            cricket_update = (
                team_1
                + " "
                + ":"
                + " "
                + t1_score
                + "\n"
                + team_2
                + " "
                + ":"
                + " "
                + "Balling"
            )
        else:
            cricket_update = (
                team_1
                + " "
                + ":"
                + " "
                + t1_score
                + "\n"
                + team_2
                + " "
                + ":"
                + " "
                + t2_score
            )

        ######################################################################################

        # sending the relevant data to the telegram user
        bot.send_message(message.chat.id, cricket_update)
    except:
        bot.send_message(
            message.chat.id, "Sorry, I am not able to get any update rn! 😢"
        )


# send joke function
@bot.message_handler(commands=["joke"])
def joke(message):

    # getting username of the telegram user
    username = str(message.chat.first_name)

    # sending the relevant data to the telegram user
    bot.send_message(
        message.chat.id,
        f"{username}, you are really gonna fall for my sense of humour 😎🤏",
    )

    time.sleep(1.5)
    bot.send_message(message.chat.id, random.choice(jokes))


# movie details function(s)
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
        api_key = ""
        # fetching the movie details from the API
        link = f"https://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
        r = requests.get(link, headers=headers)

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


# send meme function
@bot.message_handler(commands=["meme"])
def meme(message):

    try:

        # sending the relevant data to the telegram user
        bot.send_photo(message.chat.id, random.choice(memes))

    except:

        print("Some url is not working!")

        # just in case if there is some broken url it will ignore it and send the meme
        bot.send_photo(message.chat.id, random.choice(memes))


# send poem function
@bot.message_handler(commands=["poem"])
def poem(message):

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, random.choice(poems))


# send quote function
@bot.message_handler(commands=["quote"])
def quote(message):

    # sending the relevant data to the telegram user
    bot.send_message(
        message.chat.id, "Quotes are the reason why i am such a great bot 🤠"
    )
    time.sleep(1)
    bot.send_message(message.chat.id, random.choice(quotes))


# sending a random fact functionality
@bot.message_handler(commands=["fact"])
def fact(message):

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, "Here's a fact for you...")
    time.sleep(1)
    bot.send_message(message.chat.id, random.choice(facts))


# viewing top 10 western songs of the week
@bot.message_handler(commands=["topw"])
def top_western_songs(message):

    ############## getting the relevant data which is to be send by the bot ##############

    r = requests.get(western_songs_link, headers=headers)
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

    ######################################################################################

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, "Here's the 10 western songs topping the chart 🎶")
    time.sleep(0.5)
    bot.send_message(message.chat.id, top_10_western)


# viewing top 10 bollywood songs of the week
@bot.message_handler(commands=["topb"])
def top_bollywood_songs(message):

    ############## getting the relevant data which is to be send by the bot ##############

    r = requests.get(bollywood_songs_link, headers=headers)
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

    ######################################################################################

    # sending the relevant data to the telegram user
    bot.send_message(
        message.chat.id,
        "Let's see what's making buzz in the indian musical industry these days 😜",
    )
    time.sleep(2)
    bot.send_message(message.chat.id, top_10_bollywood)


# invalid command function
@bot.message_handler(func=lambda m: True)
def invalid_input(message):

    # sending the invalid command message to the telegram user
    bot.send_message(message.chat.id, "Invalid input 😕")


bot.infinity_polling()
