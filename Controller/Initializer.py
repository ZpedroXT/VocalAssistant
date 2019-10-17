

from insertData import InsertData

class Initializer:

    def __init__(self):
        self.modulesNames = ["DateInformation", "Boss"]


    def createFileCategoryOrder(self):
        ToSave = InsertData();
        myFile = "./../test/DataSet/Order/categoryOrder"
        f = open(myFile,"w+")

        modules = map(__import__, self.modulesNames)
        for module in modules:
            className = dir(module)[0]
            myClasse = getattr(module, className)
            myFunctions = dir(myClasse)
            myFunctions.remove('__doc__')
            myFunctions.remove("__init__")
            myFunctions.remove("__module__")
            print(myFunctions)

            for function in myFunctions:
                f.write(function + "|" +className+ "\n")

        f.close()
        ToSave.SaveMethodName(myFile)


test = Initializer()
test.createFileCategoryOrder()

