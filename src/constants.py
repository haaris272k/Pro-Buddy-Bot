###############################################################################################
#    Python file to store the constants, most commonly website links, used in the project.    #
###############################################################################################


# reading credentials from creds.txt file
with open("your_credentials_file.txt", "r") as f:
    keys = f.read().splitlines()

# credentials
BOT_KEY = ""
MOVIESDB_API_KEY =""
MONGODB_ATLAS_UNAME=""
MONGODB_ATLAS_PW =""

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# for trending news url
TRENDING_NEWS_LINK = "https://www.ndtv.com/trends/trends"

# for weather update url
WEATHER_UPDATE_LINK = "https://weather.com/en-IN/weather/today/l/26.80,80.89?par=google"

# western songs chart url
WESTERN_SONGS_LINK = "https://www.billboard.com/charts/billboard-global-200/"

# bollywood songs chart url
BOLLYWOOD_SONGS_LINK = (
    "https://www.jiosaavn.com/s/playlist/phulki_user/Weekly_Top_Songs/8MT-LQlP35c_"
)

INVALID_INPUT_GIF = "https://tenor.com/view/nah-no-deal-wrong-number-refuse-cross-mark-gif-12777987360130611860"

# welcoming the user
l1 = "Hi!, I am a bot that can be your 'Best Buddy' in need."
l2 = "Feel free to add me to your telegram groups and let others know about me."
l3 = "Type '/list' to see all the available commands"

# interactive messages
# greetings
interactive_greet_response = [
    "What about yourself? 😃",
    "How are you doing? 😄",
    "How have you been? 😃",
    "How's it going with you? 😄",
    "How are things on your end? 😃",
    "How's everything with you? 😄",
]

# joke response
interactive_joke_response = [
    "Careful, sometimes it might get dark 😳",
    "I'm not sure if you are gonna like it or not but, here you go 🙊",
]

# news response
interactive_news_response = [
    "Let's see the top trending news of the day 🧐",
    "Trending news of the day 📰",
    "Here's the top headlines of the day 🗞",
]


# fact response
interactive_fact_response = [
    "Here's a fact for you 🤓",
    "Did you know? 🤔",
    "Fact: 🧐",
]
