from DateInformation import DateInformation
from insertData import InsertData


class WatchFile:

    listModule = []

    def __init__(self):
        self.listModule.append(DateInformation)
        self.generateFile(self.listModule)


    def generateFile(self,Mymodules):
        ToSave = InsertData();

        # ToSave.SaveClassName(Mymodules)

        MyList = dir(Mymodules[0])

        MyList.remove('__doc__')
        MyList.remove("__init__")
        MyList.remove("__module__")

        f = open("./../test/DataSet/Order/categoryOrder", "w+")



        for aModule in MyList:
            f.write(aModule+ "|"+Mymodules[0].__name__+"\n" )



        f.close()
        ToSave.SaveMethodName("./../test/DataSet/Order/categoryOrder")




Todo = WatchFile()