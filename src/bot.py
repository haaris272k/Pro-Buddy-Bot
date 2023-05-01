from constants import *
from database_handlers import *
from data_scraper import *
import time
import telebot

# creating an instance of the TeleBot class
bot = telebot.TeleBot("BOT_KEY")

# connecting to the database from DatabaseHandler class
dbhandler.connect_database("MONGODB_ATLAS_UNAME", "MONGODB_ATLAS_PW")


@bot.message_handler(commands=["start"])
def hello(message):

    """
    function to greet the user and send the list of available commands

    Args:
        message (str): message sent by the user

    Returns:
        None
    """
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


@bot.message_handler(commands=["list"])
def list(message):

    """
    function to send the list of available commands to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
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
        + "/eg - connect to the ExpenseGenie bot."
    )

    # sending the list of commands to the telegram user
    bot.send_message(message.chat.id, comms)


@bot.message_handler(commands=["hello", "hi", "hey"])
def hello(message):

    """
    function to greet the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    # greeting the user
    username = str(message.chat.first_name)
    greet = random.choice(interactive_greet_response)
    bot.send_message(message.chat.id, f"Hey {username}, {greet}")


@bot.message_handler(commands=["nu"])
def trending_news(message):

    """
    function to send trending news to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    # using get_news() method from Data_Scraper class to get the news
    trending_news = data.get_news(TRENDING_NEWS_LINK)

    # sending the relevant data to the telegram user
    interactive_tn_response = random.choice(interactive_news_response)
    bot.send_message(message.chat.id, interactive_tn_response)
    time.sleep(0.5)
    bot.send_message(message.chat.id, trending_news)


@bot.message_handler(commands=["fun"])
def joke(message):

    """
    function to send a random joke to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
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


@bot.message_handler(commands=["meme"])
def meme(message):

    """
    function to send a random meme to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    tagtype = "meme"
    result = dbhandler.lookup(tagtype)
    bot.send_photo(message.chat.id, result)


@bot.message_handler(commands=["lit"])
def poem(message):

    """
    function to send a random poem to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    tagtype = "poem"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["quote"])
def quote(message):

    """
    function to send a random quote to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    tagtype = "quote"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["fact"])
def fact(message):

    """
    function to send a random fact to the user

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    tagtype = "fact"
    result = dbhandler.lookup(tagtype)
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["topw"])
def top_western_songs(message):

    """
    function to display top 10 trending western songs

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    # using get_trending_western_songs() method from Data_Scraper class to get the top 10 trending western songs
    top_10_western = data.get_trending_western_songs(WESTERN_SONGS_LINK)

    # sending the relevant data to the telegram user
    bot.send_message(message.chat.id, "Here's the 10 western songs topping the chart 🎶")
    time.sleep(0.5)
    bot.send_message(message.chat.id, top_10_western)


@bot.message_handler(commands=["topb"])
def top_bollywood_songs(message):

    """
    function to display top 10 trending bollywood songs

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    # using get_trending_bollywood_songs() method from Data_Scraper class to get the top 10 trending bollywood songs
    top_10_bollywood = data.get_trending_bollywood_songs(BOLLYWOOD_SONGS_LINK)

    # sending the relevant data to the telegram user
    bot.send_message(
        message.chat.id,
        "Let's see what's making buzz in the indian musical industry these days 😜",
    )
    time.sleep(2)
    bot.send_message(message.chat.id, top_10_bollywood)


@bot.message_handler(commands=["eg", "expensegenie", "EG"])
def expense_genie(message):
    """
    function to connect to the ExpenseGenie bot

    Args:
        message (str): message sent by the user

    Returns:
        None
    """
    # creating an inline keyboard to connect to ExpenseGenie bot
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(
        text="Connect to ExpenseGenie", url="https://t.me/BudgetWizardBot"
    )
    keyboard.add(url_button)

    # sending the interactive message to the telegram user
    bot.send_message(
        message.chat.id,
        "ExpenseGenie is a telegram bot that helps you to manage your expenses. \n\n"
        "Click the button below to connect to the ExpenseGenie bot:",
        reply_markup=keyboard,
    )


@bot.message_handler(func=lambda m: True)
def invalid_input(message):

    """
    function to handle invalid input

    Args:
        message (str): message sent by the user

    Returns:
        None

    """
    # sending 'invalid input!' message to the user along with the gif
    bot.send_animation(
        message.chat.id, INVALID_INPUT_GIF, caption="Unrecognizable command!"
    )


def main():

    """
    main function to run the bot

    Returns:
        None

    """
    # running the bot
    bot.polling()


if __name__ == "__main__":
    main()
