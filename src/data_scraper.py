from bs4 import BeautifulSoup
from constants import *
import requests

"""
This class has the methods which fetch the data at the real time from the various sources.
get_news method is used to fetch the news from the news website.
get_weather_update method is used to fetch the weather update from the web.
get_trending_western_songs method is used to fetch the trending (top) western songs from the music website.
get_trending_bollywood_songs method is used to fetch the trending (top) indian songs from the music website.

"""
class DataScraper:

    def __init__(self) -> None:

        """
        This is the constructor of the class.

        Args:
            self: The object of the class.

        Returns:
            None
        
        """
        pass

    def get_news(self, TRENDING_NEWS_LINK):

        """
        This method is used to fetch the news from the news website.

        Args:   
            self: The object of the class.  

        Returns:    
            final_display: The string which contains the news.
        
        """
        r = requests.get(TRENDING_NEWS_LINK)

        soup = BeautifulSoup(r.text, "html.parser")

        news = soup.find_all(
            "h3", {"class": "trenz_news_head lh22 listing_story_title"}
        )

        trending_news = []

        for i in news:

            trending_news.append(i.get_text())

        final_display = " "

        for j in trending_news[0:10]:

            final_display = final_display + "🗞" + " " + j + "\n" + "\n"

        return final_display

    # def get_weather_update(self, WEATHER_UPDATE_LINK):

        # """
        # This method is used to fetch the weather update from the web.

        # Args:   
        #     self: The object of the class.

        # Returns:
        #     weather: The string which contains the weather update.
        
        # """
        # r = requests.get(WEATHER_UPDATE_LINK, headers=HEADERS)

        # soup = BeautifulSoup(r.text, "html.parser")

        # temperature = soup.find(
        #     "span", {"class": "CurrentConditions--tempValue--3a50n"}
        # ).get_text()

        # weather = "The current temperature is" + " " + temperature + "C"

        # return weather


    def get_trending_western_songs(self, WESTERN_SONGS_LINK):

        """
        This method is used to fetch the trending (top) western songs from the music website.

        Args:
            self: The object of the class.

        Returns:
            top_10_western: The string which contains the top 10 western songs.
        
        """
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

            top_10_western = (
                top_10_western + f"{i+1}" + " " + list_songs[i] + "\n" + "\n"
            )

        return top_10_western

    def get_trending_bollywood_songs(self, BOLLYWOOD_SONGS_LINK):

        """
        This method is used to fetch the trending (top) indian songs from the music website.

        Args:
            self: The object of the class.

        Returns:
            top_10_bollywood: The string which contains the top 10 indian songs.
        
        """
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

        return top_10_bollywood

# creating an object of the class
data = DataScraper()