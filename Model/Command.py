# -*-coding:UTF-8 -*
from difflib import SequenceMatcher

import mysql.connector


class Command:


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




    def getAllCommand(self):


        self.mycursor.execute("SELECT * FROM command")

        myresult = self.mycursor.fetchall()

        return myresult


    def compareCommands(self, baseCommand):
        commands = self.getAllCommand()

        biggerRatio = 0
        for command in commands:
            ratio = SequenceMatcher(None,baseCommand, command[1]).ratio()


            if(ratio > biggerRatio ):
                bestCommand = command
                biggerRatio = ratio
                print(ratio)

        commandToCreate = [baseCommand,bestCommand[2]]
        # print(bestCommand)
        print("commande de base: "+baseCommand)
        print('Meilleur match: ' + bestCommand[1])

        if(ratio != 1 and ratio >= 0.50):
            self.createCommand(commandToCreate)

        return bestCommand




    def createCommand(self,command):



        try:
            sql = "INSERT INTO command (sequence, idRecognition) VALUES (%s, %s)"
            val = (command[0],command[1])
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            with  open("./test/DataSet/Order/order", "a") as file:
                file.write("\n"+command[0]+'|'+ str(command[1]))

        except:
            print('elle existe deja en base de donnée')

    def getAllInformation(self,command):

        # SELECT * FROM
        # command
        # INNER
        # JOIN
        # recognition
        # ON
        # command.idRecognition = recognition.id
        # INNER
        # JOIN
        # myClass
        # ON
        # recognition.idMyClass = myClass.id
        print(command)

        sql = "SELECT * FROM command INNER JOIN recognition ON command.idRecognition = recognition.id INNER JOIN myClass ON recognition.idMyclass= myClass.id where command.id = %s"
        adr = (command[0],)

        self.mycursor.execute(sql, adr)

        myresult = self.mycursor.fetchone()


        return myresult











