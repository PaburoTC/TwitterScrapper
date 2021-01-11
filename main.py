from selenium import webdriver
from time import sleep

from db import Tweet


class TBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/login")
        self.__login(username, password)
        while True:
            self.__scrap_tweets()
            self.__scroll()

    def __login(self, username, pswd):
        sleep(2)

        username_input = self.driver.find_element_by_xpath("//input[@name=\"session[username_or_email]\"]")
        username_input.send_keys(username)

        pswd_input = self.driver.find_element_by_xpath("//input[@name=\"session[password]\"]")
        pswd_input.send_keys(pswd)

        login = self.driver.find_element_by_xpath("//div[@data-testid=\"LoginForm_Login_Button\"]/div")
        login.click()

    def __scrap_tweets(self):
        try:
            sleep(2)
            tweets = self.driver.find_elements_by_xpath("//article[@role=\"article\"]")
            for tweet in tweets:
                author = tweet.find_element_by_xpath(".//div[@dir=\"ltr\"]").text
                text = tweet.find_element_by_xpath(".//div[@class=\"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 "
                                                   "r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0\"]").text
                data = tweet.find_elements_by_xpath(".//div[@class=\"css-1dbjc4n r-xoduu5 r-1udh08x\"]")
                time = tweet.find_element_by_xpath(".//time").get_attribute("datetime")

                comments = self.__format_data(data[0].text)
                retweets = self.__format_data(data[1].text)
                likes = self.__format_data(data[2].text)

                tweet = Tweet(user=author, date=time, likes=likes, retweets=retweets, comments=comments, text=text)
                tweet.add()

        except:
            self.__scroll()

    def __format_data(self, data):
        if data.__contains__("K"):
            return int(float(data.replace("K", "")) * 1000)
        if data.__contains__("M"):
            return int(float(data.replace("M", "")) * 10000000)
        return int(data)

    def __scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


TBot()
