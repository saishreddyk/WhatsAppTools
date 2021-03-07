from selenium.webdriver import Chrome, ChromeOptions
from selenium.common import exceptions
from time import sleep
from datetime import datetime


class WhatsAppKit:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("--user-data-dir=C:\\Users\\saish\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        options.add_argument("--profile-directory=Default")
        self.browser = Chrome(executable_path="chromedriver.exe", options=options)

    def spam_it(self, target, message, no_of_messages=10, send_message=True):
        """
        Control the spamming aka messaging with this feature

        :param target: The target to spam or message
        :param message: The message to be sent
        :param no_of_messages: Number of messages to send
        :param send_message: To whether send the message or wait for you to add something and send
        :return: None (things get done)
        """
        self.browser.get("https://web.whatsapp.com/")
        sleep(10)
        search_box = self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div["
                                                        "1]/div/label/div/div[2]")
        search_box.click()
        search_box.send_keys(target)
        sleep(2)
        target_id = None
        i = 1

        while target_id is None:
            try:
                target_id = self.browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div["
                    "{}]/div/div/div[2]/div[1]/div[1]/span/span/span".format(i))
            except exceptions.NoSuchElementException:
                i += 1
                pass

        if target_id.text == target:
            target_id.click()
            text_box = self.browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            for i in range(no_of_messages):
                text_box.send_keys(message)
                if send_message:
                    self.browser.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button").click()
            print("Success")

    def b_wishes(self):
        """
        This when run parses a csv file and sends birthday wishes if any..

        :return: None (well you won't forget to wish)
        """
        year, month, day = str(datetime.now())[:10].split("-")

        with open("birthDates.csv") as f:
            for i in f.readlines():
                name, f_date = i.split(",")
                f_month, f_day = f_date.split("-")
                if month == f_month and day == f_day:
                    self.spam_it(name, message="Happy Birthday ", no_of_messages=1, send_message=False)
