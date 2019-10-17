
import random

import mysql.connector




class Boss:

    def __init__(self,):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="Eva"
        )
        self.mycursor = self.mydb.cursor()
        # commands = self.getAllCommand()
        # # self.compareCommands(commands,command)


    def getPresentation(self):
        whoIam = self.whoIam()
        if len(whoIam) > 0:
            whoIam = random.choice(whoIam)
        return whoIam[1]

    def mySelfPresentation(self):
        whoIam = self.whoEva()
        whoIam = random.choice(whoIam)
        return whoIam[1]


    def whoIam(self):
        sql = "SELECT * FROM answer where type = %s "
        adr = ("%whoEva%",)

        self.mycursor.execute(sql, adr)

        myresult = self.mycursor.fetchall()

        return myresult

    def whoEva(self):
        sql = "SELECT * FROM answer where type like %s "
        adr = ("%whoEva%",)

        self.mycursor.execute(sql, adr)

        myresult = self.mycursor.fetchall()
        print("mon resultat")
        print(myresult)
        return myresult

test = Boss().getPresentation()

