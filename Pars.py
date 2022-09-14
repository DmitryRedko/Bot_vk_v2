import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup


class Pars:
    def today(self):
        current_datetime = datetime.now().weekday()
        return current_datetime

    def pars_url_current_week(self):
            RASP = "https://rasp.tpu.ru/site/department.html?id=7863&cource=3"

            headers = {'user agent': "Mozilla/5.0 (X11; Linux x86_64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/100.0.4896.127 Safari/537.36"}
            html = requests.get(RASP, headers)
            soup = BeautifulSoup(html.content, 'html.parser')
            convert = soup.findAll('a', title = "01.03.02 Прикладная математика и информатика")
           # print(convert[1])
            convert=re.findall(r"https:.+?(?=\")",str(convert[1]))
            URL=convert[0]
            return URL

    def pars_num_current_week(self):
        URL=self.pars_url_current_week()
        convert = re.findall(r"\d+?(?=/view)", str(URL))
        numweek = convert[0]
        return numweek

    def parstimetable(self,day,URL):

        headers = {'user agent': "Mozilla/5.0 (X11; Linux x86_64) "
                                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/100.0.4896.127 Safari/537.36"}
        html = requests.get(URL, headers)
        soup = BeautifulSoup(html.content, 'html.parser')
        convert = soup.findAll('td')
        #print(convert)

        Timelist = ['8.00-10.05', '10.25-12.00', '12.40-14.15', '14.35-16.10', '16.30-18.05', '18.25-20.00',
                    '20.20-21.55']

        Timetable = []

        for tim in range(0, 7):
            convert1 = convert[day + tim * 7].findAll('div')
            converted = []
            for i in convert1:
                # print(i)
                convertv2 = re.findall(r">[,]*\s*\w+\s*[.]*\w*[.]*\s*\w*[.]*<", str(i))
                for j in convertv2:
                    converted += [j[1:len(j) - 1]]
            # print(converted)
            if (bool(len(converted))):
                Timetable += [str(Timelist[tim]) + ": " + " ".join(map(str, converted))]
            else:
                Timetable += [str(Timelist[tim]) + ": " + "Окно"]
        return Timetable

    def timetable_today(self):
        day = self.today()+1
        URL = self.pars_url_current_week()
        print(day,URL)
        return self.parstimetable(day,URL)

    def timetable_tommorow(self):
        day=self.today()+2
        URL=self.pars_url_current_week()
        return self.parstimetable(day,URL)

    def thisweek(self,day):
        day=day+1
        URL = self.pars_url_current_week()
        print(day, URL)
        return self.parstimetable(day, URL)

    def nextweek(self,day):
        day=day+1
        week=self.pars_num_current_week()
        print("Неделя:",week)
        week=int(week)+1
        print("Теперь неделя:",week)
        URL = f"https://rasp.tpu.ru/gruppa_36897/2022/{week}/view.html"
        print(day, URL)
        return self.parstimetable(day,URL)


