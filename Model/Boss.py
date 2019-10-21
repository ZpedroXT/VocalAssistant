


class Boss:

    def __init__(self):
        print("")

    def whoIam(self):
        sql = "SELECT * FROM answer where sequence type = "
        adr = ("whoIam",)

        self.mycursor.execute(sql, adr)

        myresult = self.mycursor.fetchall()

        return myresult

    def whoEva(self):
        sql = "SELECT * FROM answer where sequence type = "
        adr = ("whoEva",)

        self.mycursor.execute(sql, adr)

        myresult = self.mycursor.fetchall()

        return myresult
