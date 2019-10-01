# -*-coding:UTF-8 -*

import datetime
import locale

class DateInformation:


    def __init__(self, myPhrase):
        locale.setlocale(locale.LC_TIME, '')
        #on pensera a recuperer l'information dans myPhrase et voir à quel methode elle est relié.
        print("ok")



    def getToday(self):
        today = datetime.date.today()

        # Textual month, day and year
        d2 = today.strftime("%d %B  %Y")
        print("Nous sommes le "+ d2)

        return "Nous sommes le "+ d2

    def getTomorrow(self):
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(1)
        print ("demain nous serons le: "+datetime.datetime.strftime(tomorrow, '%d %B %Y'))

        return "demain nous serons le: "+datetime.datetime.strftime(tomorrow, '%d %B %Y')

    def getYesterday(self):
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(1)
        print("hier nous etions le: " + datetime.datetime.strftime(yesterday, '%d %B %Y'))


    def getDayAtdate(self):
        print()

    def getDifferenceBetweenDate(self,d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)




