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


    def     SaveMethodName(self, myFile):

        self.deleteAllColumn(1, "recognition")
        mycursor = self.mydb.cursor()
        # try:
        f = open(myFile, "r")
        line = f.readline()
        while line:

            elementPhrase = line.split("|")
            # print(elementPhrase[0])
            # print(elementPhrase[1])




            myId = self.isExistantClass(elementPhrase[1])

            sql = "INSERT INTO recognition (methodName, idMyClass ) VALUES (%s, %s)"
            val = (elementPhrase[0], myId)
            mycursor.execute(sql, val)
            self.mydb.commit()
            line = f.readline()
        f.close()
        self.pushCommand()









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









    def isExistantClass(self,theClass):

        mycursor = self.mydb.cursor()

        sql = "SELECT count(*) FROM myClass where name = %s"
        mycursor.execute(sql, (theClass,))
        myresult = mycursor.fetchone()

        if (myresult[0] < 1 ):

            sql = "INSERT INTO myClass (name) VALUES (%s)"
            mycursor.execute(sql, (theClass,))

        sql = "SELECT * FROM myClass where name = %s"
        mycursor.execute(sql, (theClass,))
        myresult = mycursor.fetchone()

        return myresult[0]



    def pushCommand(self):

        self.deleteAllColumn(1, "command")
        mycursor = self.mydb.cursor()
        # try:

        f = open("./../test/DataSet/Order/order", "r")

        line = f.readline()
        while line:
            #print(line)
            elementPhrase = line.split("|")
            # print(elementPhrase[0])

            myId = self.findMethodId(elementPhrase[1])

            sql = "INSERT INTO command (sequence, idRecognition ) VALUES (%s, %s)"
            val = (elementPhrase[0], myId)
            mycursor.execute(sql, val)
            self.mydb.commit()
            line = f.readline()
        f.close()
        self.pushAnswer()


    def pushAnswer(self):
        self.deleteAllColumn(1, "answer")
        mycursor = self.mydb.cursor()
        # try:

        f = open("./../test/DataSet/Order/answer", "r")

        line = f.readline()
        while line:
            # print(line)
            elementPhrase = line.split("|")
            # print(elementPhrase[0])
            # print("nom de la méthode " + elementPhrase[1])

            myId = self.findAnswerId(elementPhrase[0])
            if(myId == 0):

                sql = "INSERT INTO answer (sequence, type ) VALUES (%s, %s)"
                val = (elementPhrase[0], elementPhrase[1])
                print(val)
                mycursor.execute(sql, val)
                self.mydb.commit()
                line = f.readline()
        f.close()

    def findMethodId(self,methodeName):
        mycursor = self.mydb.cursor()

        sql = "SELECT * FROM recognition where  methodName = %s"
        mycursor.execute(sql, (methodeName.strip(),))
        myresult = mycursor.fetchone()
        try:
            return  myresult[0]
        except:
            return 0



    def findAnswerId(self,methodeName):
        mycursor = self.mydb.cursor()

        sql = "SELECT count(*) FROM answer where  sequence = %s"
        mycursor.execute(sql, (methodeName,))
        myresult = mycursor.fetchone()
        return  myresult[0]



