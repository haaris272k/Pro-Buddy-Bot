from bs4 import BeautifulSoup
from data import *
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
    l1 = "Hello, My name is Harry. My official name is 'ProBuddyBot'."
    l2 = "I'm a telegram bot that can be your best Buddy in need."
    l3 = "I can provide you with necessary updates and help you increase your Productivity."
    l4 = "Feel free to add me to your groups and let others know about me"
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


@bot.message_handler(commands=["list"])
def list(message):
    comms = (
        "List of available commands:"
        + "\n"
        + "/hi - to greet the bot."
        + "\n"
        + "/nu - to view the trending news of the day."
        + "\n"
        + "/wu - to view the live weather update."
        + "\n"
        + "/cu - to view the live cricket score."
        + "\n"
        + "/joke - to get a random joke."
        + "\n"
        + "/meme - to get a random meme."
        + "\n"
        + "/poem - to get a random poem."
        + "\n"
        + "/quote - to get a random quote."
        + "\n"
        + "/fact - to get a random fact."
        + "\n"
        + "/topw - to see the top 10 trending western songs of the week."
        + "\n"
        + "/topb-  to see the top 10 trending bollywood songs of the week."
    )
    bot.send_message(message.chat.id, comms)


@bot.message_handler(commands=["hello", "hi", "hey"])
def hello(message):
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

    """location = soup.find(
        "h1", {"class": "CurrentConditions--location--kyTeL"}
    ).get_text()"""

    temperature = soup.find(
        "span", {"class": "CurrentConditions--tempValue--3a50n"}
    ).get_text()
    condition = soup.find(
        "div", {"class": "CurrentConditions--phraseValue--2Z18W"}
    ).get_text()
    weather = (
        # "Your location is"
        # + " "
        # + location
        # + "\n"+
        "The current temperature is"
        + " "
        + temperature
        + "C"
        + " \n"
        + "It's kinda "
        + condition
        + " out there"
    )

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
    bot.send_message(message.chat.id, "Here's a fact for you 😉")
    time.sleep(1)
    bot.send_message(message.chat.id, random.choice(facts))


# showing top 10 western songs of the week
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
    bot.send_message(message.chat.id, "Looks like someone is in the mood to party 😈")
    time.sleep(1)
    bot.send_message(message.chat.id, "Here's the 10 western songs topping the chart 🎶")
    time.sleep(0.5)
    bot.send_message(message.chat.id, top_10_western)


# showing top 10 bollywood songs of the week
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
        "Oh cool bollywood!, Let's see what's making buzz in the indian musical industry these days 😜",
    )
    time.sleep(2)
    bot.send_message(message.chat.id, top_10_bollywood)


# To send some media if a user enters a wrong command
@bot.message_handler(func=lambda m: True)
def repeat(message):

    # randomly choosing a media to send it to the user when he enters a wrong command
    selected_cute_media = random.choice(cute_media_collection)

    # sending the media to the telegram user
    bot.send_message(message.chat.id, "Ooopsie, You've entered the wrong command 😕")
    time.sleep(1.5)
    bot.send_message(
        message.chat.id, "It's not a problem, let me get a smile on your face 😉"
    )
    time.sleep(1.3)

    # checking if the selected media is a photo or a video
    if selected_cute_media[-3:] == "gif":
        bot.send_animation(message.chat.id, selected_cute_media)
    else:
        bot.send_photo(message.chat.id, selected_cute_media)


bot.infinity_polling()
