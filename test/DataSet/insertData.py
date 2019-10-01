# -*-coding:UTF-8 -*

import mysql.connector

class InsertData:



    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="Eva"
        )

    def insertAnswer(self, Myphrases = []):


        self.deleteAllColumn( 1,"reponse" )
        mycursor = self.mydb.cursor()


        Myphrases = self.Myfile("answer")
        for Myphrase in Myphrases:
            sql = "INSERT INTO reponse (answer, typeAnswer) VALUES (%s, %s)"
            val = (Myphrase, "1")
            mycursor.execute(sql, val)

            self.mydb.commit()

            print(mycursor.rowcount, "record inserted.")

    def deleteAllColumn(self,toDelete,tableName):

        if toDelete == 1:
            mycursor = self.mydb.cursor()

            sql = "TRUNCATE TABLE  "+tableName

            mycursor.execute(sql)

            self.mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")

    def insertOrder(self,Myphrases):
        print("ok")






    def Myfile(self,filename):
        f = open("Order/"+filename, "r")
        f1 = f.readlines()
        MyPhrase= []
        for line in f1:
            MyPhrase.append(line)

        return MyPhrase





Insertion = InsertData()

Insertion.insertAnswer()
from difflib import SequenceMatcher

a = "donne moi le jour de demain"
b = "dis moi quel jour nous sommes "

ratio = SequenceMatcher(None, a, b).ratio()
print(ratio)