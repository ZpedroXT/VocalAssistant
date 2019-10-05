# -*-coding:UTF-8 -*


import mysql.connector

class Answer:


    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="Eva"
        )




    def getAllAnswers(self,type):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT sequence FROM answer where type like '%"+type+"%'")

        myresult = mycursor.fetchall()
        print(myresult[0][0])
        MyAnswer = []
        for result in myresult:
            print(result)
            MyAnswer.append(result[0])


        return MyAnswer

    def setNewAnswer(self, answer):
        print("ok")
        #set new answer






